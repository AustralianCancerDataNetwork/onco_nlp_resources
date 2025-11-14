# Performance status

## 1. Endpoint Definition

**Description:**  
Performance status is a clinician-assigned score that summarises a patient’s functional capacity.

The most widely used scale is ECOG Performance Status (0–5):

| ECOG | Definition                                                 |
| ---- | ---------------------------------------------------------- |
| 0    | Fully active; no restrictions                              |
| 1    | Restricted in physically strenuous activity but ambulatory |
| 2    | Ambulatory >50% of waking hours; unable to work            |
| 3    | Limited self-care; >50% of time in bed/chair               |
| 4    | Completely disabled                                        |
| 5    | Dead                                                       |

**Relevant Background & Links:**
- Oken, M. M., Creech, R. H., Tormey, D. C., Horton, J., Davis, T. E., McFadden, E. T., & Carbone, P. P. (1982). Toxicity and response criteria of the Eastern Cooperative Oncology Group. American journal of clinical oncology, 5(6), 649-656.

**Cancer Domains:**  
- Any / All 

**Endpoint Type:**  
- EAV

**Endpoint Status:**  

| Assessment               | Details                                                     |
| ------------------------ | ----------------------------------------------------------- |
| **Feasibility**          | Generally feasible — ECOG typically expressed explicitly (e.g., “ECOG 1”, “PS: 0–1”). |
| **Priority**             | High priority — required for trial / treatment eligibility, prognostic modelling, and risk adjustment across most cancers.|
| **Maturity / Current State** | Prototype regex and lightweight phrase matcher exist at some sites; notebooks and heuristics shared informally; no consolidated cross-site tool yet. |
| **Shareability**   | High — ECOG terminology and phrasing are consistent across oncology documentation; minimal site-specific tuning expected. |

---

## 2. Examples
### 2.1 Positive Examples
**Example Clinical Phrasing:**  
- Performance status 2
- ECOG: 0–1

### 2.2 Negative / Exclusions
- Some notes use descriptive phrases e.g. _Patient reports minimal exertional dyspnea_
    - Current solutions do not infer PS from descriptions alone without valid and explicit physician-assessed score
    - Open-ended nature of these assessments likely to induce high degree of hallucination in LLM applications and too heterogeneous for heuristic approach

### 2.3 General Guidelines for Disambiguation
- Range will always resolve to the higher of the two scores (e.g. PS 1-2 will be extracted as score = 2)

---

## 3. Mapping to CDM
**What exactly must the NLP pipeline output?**  
> Specify format and constraints.

**Structured Output Format:**  
```json
{
    "measurement": {  
        "person_id": 1,
        "measurement_id": 2,
        "measurement_concept_id": 36305384,
        "measurement_date": "2025-11-13",
        "value_as_number": 3
    }
}
```

---

### 4. Existing Work

**Current Solutions or Prototypes:**

Demo binder: https://github.com/gkennos/ecog_nlp_demo

**Implementations in Use:**

> Include performance evaluations if available

---

## 5. Proposed Approach

**Rule-based / Heuristic Approach**

> * List key patterns or features
> * Example regex/patterns
> * Expected performance / challenges
