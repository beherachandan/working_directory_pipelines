#!/usr/bin/env bash
# generate-brief.sh — Generate a Discovery Prep Brief for an account
# Usage: ./generate-brief.sh "District/School Name"
# Requires: GOOGLE_APPLICATION_CREDENTIALS to be set
# Queries: wayagent_GTM.account_feature_store

set -euo pipefail

if [ -z "${1:-}" ]; then
  echo "Usage: $0 \"District or School Name\""
  echo "Example: $0 \"Miami-Dade County Public Schools\""
  exit 1
fi

ACCOUNT_NAME="$1"

if [ -z "${GOOGLE_APPLICATION_CREDENTIALS:-}" ]; then
  export GOOGLE_APPLICATION_CREDENTIALS="/home/ec2-user/.openclaw/workspace/bigquery-credentials.json"
fi

if [ ! -f "$GOOGLE_APPLICATION_CREDENTIALS" ]; then
  echo "ERROR: Credentials file not found at $GOOGLE_APPLICATION_CREDENTIALS"
  exit 1
fi

echo "=============================================="
echo "  DISCOVERY PREP BRIEF"
echo "  Account: $ACCOUNT_NAME"
echo "  Generated: $(date -u '+%Y-%m-%d %H:%M UTC')"
echo "=============================================="
echo ""

python3 << 'PYEOF'
import sys
from google.cloud import bigquery

client = bigquery.Client(project="quizizz-org")
account_name = sys.argv[1] if len(sys.argv) > 1 else """ACCOUNT_NAME_PLACEHOLDER"""

# Use environment variable passed from bash
import os
account_name = os.environ.get("ACCOUNT_NAME_SEARCH", account_name)

query = f"""
SELECT
  nces_id,
  entity_type,
  name,
  state,
  product_usage.active_teachers,
  product_usage.rostered_teachers,
  product_usage.logged_in_teachers,
  product_usage.total_sessions,
  product_usage.total_responses,
  product_usage.total_players,
  product_usage.classroom_sessions,
  product_usage.assessment_sessions,
  product_usage.assessment_teachers,
  product_usage.teachers_using_accommodations,
  product_usage.AI_powered_resources,
  product_usage.resources,
  product_usage.is_PQA,
  product_usage.is_paid_org,
  product_usage.top_1_teacher_full_name,
  product_usage.top_2_teacher_full_name,
  product_usage.top_3_teacher_full_name,
  ARRAY_LENGTH(board_meetings) as board_meeting_count,
  ARRAY_LENGTH(contacts) as contact_count
FROM `quizizz-org.wayagent_GTM.account_feature_store`
WHERE LOWER(name) LIKE LOWER('%{account_name}%')
LIMIT 5
"""

try:
    results = client.query(query).result()
    rows = list(results)
except Exception as e:
    print(f"Query error: {e}")
    sys.exit(1)

if not rows:
    print(f"No accounts found matching: {account_name}")
    print("Try a broader search term or check the account name spelling.")
    sys.exit(0)

for i, row in enumerate(rows):
    if i > 0:
        print("\n----------------------------------------------\n")

    print(f"## Account: {row.get('name', 'N/A')}")
    print(f"   NCES ID: {row.get('nces_id', 'N/A')}")
    print(f"   Type: {row.get('entity_type', 'N/A')}")
    print(f"   State: {row.get('state', 'N/A')}")
    is_paid = row.get('is_paid_org')
    print(f"   Paid Org: {'Yes' if is_paid else 'No'}")
    print("")

    # Product usage
    active = row.get('active_teachers') or 0
    rostered = row.get('rostered_teachers') or 0
    logged_in = row.get('logged_in_teachers') or 0
    sessions = row.get('total_sessions') or 0
    players = row.get('total_players') or 0
    classroom = row.get('classroom_sessions') or 0
    assessment = row.get('assessment_sessions') or 0
    assess_teachers = row.get('assessment_teachers') or 0
    accomm = row.get('teachers_using_accommodations') or 0
    ai_resources = row.get('AI_powered_resources') or 0
    total_resources = row.get('resources') or 0

    print("### Product Usage")
    print(f"   Rostered Teachers: {rostered}")
    print(f"   Logged-in Teachers: {logged_in}")
    print(f"   Active Teachers: {active}")
    print(f"   Total Sessions: {sessions}")
    print(f"   Classroom Sessions: {classroom}")
    print(f"   Assessment Sessions: {assessment}")
    print(f"   Assessment Teachers: {assess_teachers}")
    print(f"   Total Players: {players}")
    print(f"   Total Responses: {row.get('total_responses') or 0}")
    print(f"   Teachers Using Accommodations: {accomm}")
    print(f"   AI-Powered Resources: {ai_resources} / {total_resources} total")
    print("")

    is_pqa = row.get('is_PQA')
    if is_pqa:
        print(f"   ✅ PQA Status: YES (Pre-Qualified Adopter)")
    elif active >= 5:
        print(f"   ✅ PQA Signal: {active} active teachers (meets threshold)")
    else:
        print(f"   ❌ PQA Status: NO ({active} active teachers — below 5 threshold)")
    print("")

    # Top teachers
    top_teachers = [
        row.get('top_1_teacher_full_name'),
        row.get('top_2_teacher_full_name'),
        row.get('top_3_teacher_full_name')
    ]
    top_teachers = [t for t in top_teachers if t]
    if top_teachers:
        print("### Top Teachers (Potential Champions)")
        for j, t in enumerate(top_teachers, 1):
            print(f"   {j}. {t}")
        print("")

    # Board meetings
    bm_count = row.get('board_meeting_count', 0) or 0
    print("### Board Meeting Data")
    print(f"   Board Meetings Available: {bm_count}")
    if bm_count > 0:
        print("   → Run detailed query to extract topics and map to value props:")
        nces = row.get('nces_id', '')
        print(f"   → SELECT bm.meeting_date, bm.statement_title, bm.human_readable_summary,")
        print(f"          bm.gtm_relevance_score, bm.wayground_opportunity")
        print(f"     FROM `wayagent_GTM.account_feature_store`, UNNEST(board_meetings) bm")
        print(f"     WHERE nces_id = '{nces}'")
        print(f"     ORDER BY bm.gtm_relevance_score DESC LIMIT 10")
    else:
        print("   → No board meeting data — use general district priorities")
    print("")

    # Contacts
    print(f"### Contacts: {row.get('contact_count', 0) or 0} on file")
    print("")

    # Recommended approach
    print("### Recommended Approach")
    if is_paid:
        print("   Strategy: RENEWAL / EXPANSION — already a customer")
        print("   Lead with: Usage data, expansion signals, upcoming renewal")
        print("   See: talk-tracks/cs-renewal.md")
    elif active >= 5:
        print("   Strategy: WARM OUTREACH — strong organic adoption (PQA)")
        print("   Lead with: Teacher usage data, paywall signals, champion stories")
        print("   Persona: Start with principal/curriculum director, escalate to superintendent")
        print("   See: talk-tracks/bdr-outbound.md (warm templates)")
    elif active > 0:
        print("   Strategy: WARM OUTREACH — early adoption signals")
        print("   Lead with: Teacher activity + growth potential")
        print("   Persona: Start with teacher champions, build grassroots case")
        print("   See: talk-tracks/bdr-outbound.md (warm templates)")
    else:
        print("   Strategy: COLD OUTREACH — no product usage detected")
        if bm_count > 0:
            print("   Lead with: Board meeting priorities aligned to Wayground value props")
        else:
            print("   Lead with: Peer district references and general value proposition")
        print("   Persona: Start with superintendent or curriculum director")
        print("   See: talk-tracks/bdr-outbound.md (cold templates)")
    print("")

    # Discovery questions
    print("### Discovery Questions (Customize Before Call)")
    print('   1. "What are your top instructional technology priorities this year?"')
    print('   2. "How are you currently handling formative assessment across buildings?"')
    if active > 0:
        print(f'   3. "Did you know {active} teachers are already using Wayground? What\'s driving that adoption?"')
    else:
        print('   3. "How do teachers in your district currently discover and adopt new tools?"')
    if assessment > 0:
        print(f'   4. "{assess_teachers} teachers are running assessments — do you have visibility into that data?"')
    else:
        print('   4. "What data do you currently have visibility into at the district/building level?"')
    print('   5. "When is your budget cycle for instructional technology?"')
    print("")

print("==============================================")
print("  NEXT STEPS")
print("  1. Review board meeting details (if available)")
print("  2. Check Salesforce for deal history")
print("  3. Identify specific champion teachers")
print("  4. Select persona-appropriate talk track")
print("  5. Prepare tailored demo or meeting agenda")
print("==============================================")
PYEOF
