# Signal Sources Reference

## Category Seeds (Track 1)

These are **stable structural categories** of K-12 education — not specific topics. They define the space DataForSEO expands from. The categories stay fixed; the rising child topics within them are the signal.

### Validated seeds (empirically tested against Google Trends via DataForSEO)

```
reading instruction
writing instruction
differentiated instruction
formative assessment
social emotional learning
project based learning
inquiry based learning
phonics instruction
learning disabilities
STEM education
student engagement
educational technology
classroom behavior
```

### Why these 13

Each was tested against SEMrush `phrase_related` with KD < 40 filter. They return genuine K-12 pedagogy topics (e.g. `reading instruction` → science of reading strategies, dyslexia interventions, structured literacy; `writing instruction` → Hochman method, writing revolution, science of writing). No brand pollution.

### Seeds that were tested and rejected (do NOT use)

| Seed | Problem |
|---|---|
| `classroom management` | 95% Google Classroom typos/login queries |
| `science instruction` | Returns nothing |
| `classroom technology` | Google Classroom / unblocked games noise |
| `teaching strategies` | Teaching Strategies GOLD platform logins |
| `student assessment` | Edulastic / NWEA login typos |
| `student mental health` | Returns mostly college, not K-12 |
| `lesson planning` | Only evergreen how-to queries, no emerging signal |
| `special education strategies` | Returns nothing in Google Trends |
| `student engagement strategies` | Returns nothing in Google Trends |
| `ed tech tools for teachers` | Returns nothing in Google Trends |
| `curriculum planning` | Only 3 results, too sparse |
| `math instruction` | Returns only `differentiated instruction`, no math-specific signal |
| `behavior management` | Pulled into organizational behavior / management noise |
| `math teaching` | Dominated by AI math solver queries (not pedagogy) |
| `curriculum design` | Dominated by EdTech jobs/careers noise |
| `teacher professional development` | Too sparse (6 results) |

**Do not add specific topics as seeds** (e.g. "phonemic awareness", "AI lesson plans") — that becomes sub-theme discovery (A1's job), not emerging topic detection.

**Do not add broad terms** (e.g. "education", "teachers", "students") — too broad, returns brand navigation noise.

### Adding new seeds

Before adding any new seed, test it with SEMrush `phrase_related` + KD < 40 filter. A good seed:
- Returns 15+ distinct K-12 pedagogy terms (not brand names or login queries)
- Has no major EdTech product with a similar name (avoids brand collision)
- Is phrased as a practice/function, not a product or role

---

## Track 2 Tavily Query Templates (Upstream Signals)

All queries: use `time_range: "month"` unless noted.

### Policy and regulatory
```
# Direct source targeting
include_domains: ed.gov, congress.gov
query: new guidance OR requirement OR framework K-12 teachers 2025

# Broader coverage
"Department of Education" new policy teachers classroom 2025
state education "new requirement" OR "new framework" K-12 2025
education legislation passed 2025 classroom impact
```

### Academic research
```
include_domains: eric.ed.gov, rand.org, brookings.edu, learningpolicyinstitute.org, nces.ed.gov
query: new study findings classroom teachers K-12 2025

# Broader
"evidence-based" new teaching approach K-12 2025
education research "implications for teachers" 2025
```

### Conference agendas
```
ISTE 2025 conference sessions topics agenda
ASCD 2025 annual conference sessions emerging
SXSWedu 2025 topics sessions
NAESP OR NASSP 2025 conference agenda topics
```
Note: Session *clusters* are the signal — 5+ sessions on the same theme = strong institutional bet.

### Grant funding
```
"Department of Education" grant awarded 2025 classroom teachers
"Gates Foundation" education grant initiative 2025
"Chan Zuckerberg Initiative" education 2025
EdTech grant funded K-12 2025
```

---

## Track 3 Tavily Query Templates (Reddit Discourse)

All queries: `time_range: "month"`.

### Adoption signals
```
site:reddit.com/r/Teachers "anyone else using"
site:reddit.com/r/Teachers "just started using"
site:reddit.com/r/Teachers "changed how I teach"
site:reddit.com/r/Teachers "has anyone tried"
site:reddit.com/r/Teachers "game changer"
site:reddit.com/r/TeacherTech "started using" OR "new tool"
```

### Problem/gap signals (unmet needs)
```
site:reddit.com/r/Teachers "struggling with" OR "how do you handle"
site:reddit.com/r/Teachers "looking for a way to"
site:reddit.com/r/education "anyone have resources for"
site:reddit.com/r/SpecialEducation "looking for" OR "anyone know"
```

Problem threads with no clear solutions surfacing = content gap Wayground can own before anyone else.

---

## Noise Filter

### Always exclude
- Named individuals (teachers, politicians, researchers, celebrities)
- State-specific standardized tests: STAAR (TX), MCAS (MA), CMAS (CO), ILEARN (IN), MILESTONES (GA), SOL (VA), CAASPP (CA), PARCC, SBAC, and other state-specific assessments
- Competitor brand names used as navigational queries: Khan Academy, Quizlet, Teachers Pay Teachers, Kahoot, Nearpod, Duolingo
- Jobs/careers/HR: teacher salary, teacher hiring, ed tech jobs, substitute teacher
- Higher education: college, university, undergraduate, grad school, FAFSA
- Corporate/adult learning: employee training, corporate L&D, workplace learning
- Seasonal calendar queries (confirm by checking if volume spike is date-driven, not structural)
- Single news-cycle spikes with no classroom content angle

### Keep with care
- Policy/framework terms (NGSS, IEP, RTI, MTSS, PBIS) — keep; writeable content angles exist
- Platform names (Google Classroom, Canvas, Seesaw) — keep only if the query has an instructional usage angle, not just the brand name
- Research/cognitive terms (metacognition, retrieval practice, spaced repetition) — keep; strong long-tail AEO value

---

## Volume Thresholds

| Tier | Volume range | Notes |
|---|---|---|
| Sweet spot | 100–2,000/mo | Growing from low base; pre-competitive |
| Early signal | 50–100/mo | Include if strong MoM or upstream signal |
| Pre-search | 0–50/mo | Keep if Track 2 or Track 3 signal is strong — publish now |
| Saturated (KW's job) | > 3,000/mo | Out of scope for this skill |

---

## DataForSEO Tool Names (confirm at runtime)

Common names from `@dataforseo/mcp-server`:
- `dataforseo_labs_google_keyword_ideas`
- `dataforseo_labs_google_related_keywords`
- `dataforseo_labs_google_historical_keyword_data`
- `dataforseo_labs_google_keyword_suggestions`

If exact names differ, use the closest equivalent that returns `monthly_searches` (12-month volume array).
