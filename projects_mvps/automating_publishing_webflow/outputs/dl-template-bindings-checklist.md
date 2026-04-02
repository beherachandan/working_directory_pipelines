# DL Template CMS Field Bindings Checklist

Template page ID: `69ca46c801a5a26e0c8d8f30`
Collection: Differentiated Learning (`69ca46c801a5a26e0c8d8f22`)

Open Designer → navigate to DL template → click each element below and verify "Get value from" in the right panel.

---

## Page-level bindings

- [ ] **SEO Title** (Page Settings → SEO tab) → `meta-title-seo`
- [ ] **SEO Description** (Page Settings → SEO tab) → `meta-description-seo`

---

## blog_template-section

- [ ] `blog_temp-category .text-size-large-bold` → `category` (name field)
- [ ] `blog_template-heading` (H1) → `name`
- [ ] `blog_temp-info-text` (first date div inside `blog_temp-info-text-wrap`) → `publishing-date`
- [ ] `blog_hero-img` (Image) → `main-image`
- [ ] `main-image-visible` conditional visibility on `blog_hero-img` → `main-image-visible` (Switch field)

---

## blog_template-wrapper

- [ ] `text-rich-text` (RichText inside `blog_template-summary-wrap`) → `content`

---

## faq_section

- [ ] `faq_heading` (H2 inside `faq_heading_wrapper`) → `faq-title`
- [ ] `faq_collection_list` (DynamoWrapper) → connected to DL collection, field: `faqs` (MultiReference)
  - [ ] DynamoList inner structure: `faq_ilist` list → `faq` item → accordion elements bound to FAQ collection fields (`question`, `answer`)

---

## discover_blog-card-section

- [ ] `collection_list-wrapper` (DynamoWrapper) → connected to DL collection (for "More Articles" related posts)
  - [ ] `blog_card` link → href bound to item URL
  - [ ] `blog_card-img` → article image field
  - [ ] blog card text elements → article name/category fields

---

## Notes

- Bindings that still reference QT collection fields will silently pull wrong data — check each one
- `faq_collection_list` DynamoWrapper is the highest-risk binding (multi-ref vs direct collection)
- If any binding shows "No field connected" or references `69722f7dd5ea1f81a678f394` (QT collection ID), it needs to be re-mapped to `69ca46c801a5a26e0c8d8f22`
