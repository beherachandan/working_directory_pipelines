"""Create Google Drive folders and write Google Docs via service account."""
import logging
import time

logger = logging.getLogger(__name__)

FOLDER_MIME = "application/vnd.google-apps.folder"
DOC_MIME = "application/vnd.google-apps.document"

SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/documents",
]


def _get_credentials(service_account_json: str):
    from google.oauth2.service_account import Credentials
    return Credentials.from_service_account_file(service_account_json, scopes=SCOPES)


def get_drive_service(service_account_json: str):
    from googleapiclient.discovery import build
    creds = _get_credentials(service_account_json)
    return build("drive", "v3", credentials=creds)


def get_docs_service(service_account_json: str):
    from googleapiclient.discovery import build
    creds = _get_credentials(service_account_json)
    return build("docs", "v1", credentials=creds)


def get_or_create_folder(drive_service, folder_name: str, share_email: str = "") -> str:
    """
    Return folder_id for a Drive folder with the given name.
    Creates it if not found. Shares with share_email if provided.
    """
    # Search for existing folder (owned by service account)
    query = f"name='{folder_name}' and mimeType='{FOLDER_MIME}' and trashed=false"
    results = drive_service.files().list(q=query, fields="files(id, name)").execute()
    files = results.get("files", [])

    if files:
        folder_id = files[0]["id"]
        logger.info(f"Found existing Drive folder: {folder_name} ({folder_id})")
    else:
        metadata = {"name": folder_name, "mimeType": FOLDER_MIME}
        folder = drive_service.files().create(body=metadata, fields="id").execute()
        folder_id = folder["id"]
        logger.info(f"Created Drive folder: {folder_name} ({folder_id})")

    if share_email:
        try:
            drive_service.permissions().create(
                fileId=folder_id,
                body={"type": "user", "role": "writer", "emailAddress": share_email},
                sendNotificationEmail=False,
            ).execute()
            logger.info(f"Shared folder with {share_email}")
        except Exception as e:
            logger.warning(f"Could not share folder with {share_email}: {e}")

    return folder_id


def audit_storage(drive_service) -> dict:
    """
    Return SA's Drive storage info and list of owned files sorted by size.
    Read-only — makes no changes.
    """
    about = drive_service.about().get(
        fields="storageQuota,user"
    ).execute()
    quota = about.get("storageQuota", {})
    user = about.get("user", {})

    files_result = drive_service.files().list(
        fields="files(id,name,size,mimeType,createdTime)",
        orderBy="quotaBytesUsed desc",
        pageSize=50,
        q="trashed=false",
    ).execute()

    return {
        "user_email": user.get("emailAddress", ""),
        "limit_bytes": int(quota.get("limit", 0)),
        "used_bytes": int(quota.get("usage", 0)),
        "used_in_drive_bytes": int(quota.get("usageInDrive", 0)),
        "files": files_result.get("files", []),
    }


def copy_doc(drive_service, source_doc_id: str, new_title: str, folder_id: str) -> str:
    """
    Copy an existing Google Doc into folder_id with new_title.
    Returns the new doc_id. The copy is initially owned by the service account.
    """
    body = {"name": new_title, "parents": [folder_id]}
    result = drive_service.files().copy(
        fileId=source_doc_id,
        body=body,
        fields="id",
        supportsAllDrives=True,
    ).execute()
    doc_id = result["id"]
    logger.info(f"Copied doc {source_doc_id} → {doc_id} ({new_title})")
    return doc_id


def apply_text_replacements(docs_service, doc_id: str, replacements: list[dict]):
    """
    Apply a list of find-and-replace operations to a Google Doc.
    Each replacement dict: {old_text: str, new_text: str, match_case: bool}
    """
    if not replacements:
        return
    requests = [
        {
            "replaceAllText": {
                "containsText": {
                    "text": r["old_text"],
                    "matchCase": r.get("match_case", True),
                },
                "replaceText": r["new_text"],
            }
        }
        for r in replacements
        if r.get("old_text") and r["old_text"] != r.get("new_text", "")
    ]
    if requests:
        docs_service.documents().batchUpdate(
            documentId=doc_id,
            body={"requests": requests},
        ).execute()
        logger.info(f"Applied {len(requests)} text replacements to {doc_id}")


def append_aeo_section(docs_service, doc_id: str, content: str):
    """
    Append a clearly marked AEO additions section at the end of the document body.
    content: plain text / markdown of the additions.
    """
    if not content.strip():
        return

    separator = "\n\n\u2500" * 30 + "\n"
    header = "\u270f\ufe0f AEO ADDITIONS \u2014 PLACE IN DOCUMENT\n"
    full_text = separator + header + content.strip() + "\n"

    # Get current doc to find end index
    doc = docs_service.documents().get(documentId=doc_id).execute()
    body = doc.get("body", {})
    content_items = body.get("content", [])
    end_index = content_items[-1].get("endIndex", 1) - 1 if content_items else 1

    docs_service.documents().batchUpdate(
        documentId=doc_id,
        body={"requests": [
            {"insertText": {"location": {"index": end_index}, "text": full_text}}
        ]},
    ).execute()
    logger.info(f"Appended AEO section to {doc_id}")


def transfer_ownership(drive_service, file_id: str, email: str) -> bool:
    """
    Transfer ownership of a Drive file to email.
    Returns True on success, False if cross-domain transfer is not allowed.
    """
    try:
        drive_service.permissions().create(
            fileId=file_id,
            body={"type": "user", "role": "owner", "emailAddress": email},
            transferOwnership=True,
            sendNotificationEmail=False,
        ).execute()
        logger.info(f"Transferred ownership of {file_id} to {email}")
        return True
    except Exception as e:
        # Fall back to writer permission so the user can still access the doc
        logger.warning(f"Ownership transfer failed ({e}); granting writer access instead")
        try:
            drive_service.permissions().create(
                fileId=file_id,
                body={"type": "user", "role": "writer", "emailAddress": email},
                sendNotificationEmail=False,
            ).execute()
        except Exception as e2:
            logger.warning(f"Could not grant writer access either: {e2}")
        return False


def create_doc_in_folder(
    drive_service,
    docs_service,
    title: str,
    content: str,
    folder_id: str,
) -> str:
    """
    Create a Google Doc inside folder_id with the given title and plain-text content.
    Returns the doc URL.
    """
    # 1. Create blank doc inside the folder
    metadata = {
        "name": title,
        "mimeType": DOC_MIME,
        "parents": [folder_id],
    }
    doc_file = drive_service.files().create(body=metadata, fields="id").execute()
    doc_id = doc_file["id"]

    # 2. Insert content via Docs batchUpdate
    # Docs API insertText requires index 1 (after the implicit paragraph at index 0)
    # Split into chunks to stay under the 1MB request limit
    MAX_CHUNK = 40000  # characters
    chunks = [content[i:i + MAX_CHUNK] for i in range(0, len(content), MAX_CHUNK)]

    insert_index = 1
    requests = []
    for chunk in chunks:
        requests.append({
            "insertText": {
                "location": {"index": insert_index},
                "text": chunk,
            }
        })
        insert_index += len(chunk)

    if requests:
        docs_service.documents().batchUpdate(
            documentId=doc_id,
            body={"requests": requests},
        ).execute()

    doc_url = f"https://docs.google.com/document/d/{doc_id}/edit"
    logger.info(f"Created doc: {title} → {doc_url}")
    return doc_url
