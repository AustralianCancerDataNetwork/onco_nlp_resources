# Radiotherapy Site/Region

---

## 1. Endpoint Definition

**Description:**  
Radiotherapy regions describe the anatomical targets to which radiation treatment is delivered (e.g., lung apex, mediastinum, pelvis, neck, brain). They are typically documented in short text fields, although the practice may vary by vendor.  

Radiation therapy (RT) regions and fields are highly patient-specific. These elements often require custom terminology to capture precise tumour locations and geometries and rarely map to structured data fields via established standards. 

**Relevant Background & Links:**  
- 

**Cancer Domains:**  
- 

**Endpoint Type:**  
- Categorical

**Endpoint Status:**  

| Assessment | Details |
|-----------|---------|
| **Feasibility** | Regions are usually explicitly labelled (e.g., “left lung PTV”, “neck level II–IV”), but terminology varies across providers and vendors. Good feasibility from short targeted fields specific to RT region; moderate feasibility from general notes. Modifiers such as laterality, sub-region may obscure. |
| **Priority** | High — radiotherapy region is essential for toxicity modelling, organ-at-risk analysis, recurrence studies, and complete treatment trajectory reconstruction. |
| **Maturity / Current State** | Prototype lightweight LLM region mapper exists. Requires refinement for cross-site terminology differences. |
| **Shareability** | High — radiation oncology uses internationally standardised anatomic terms; region dictionaries can be harmonised with minimal local tuning. |

---

## 2. Examples

### 2.1 Positive Examples  
- “ph1 prostate”  
- “t11-l3”  
- “(r) breast/low axilla”

### 2.2 Negative / Exclusions
- This pipeline is designed to handle short targeted text snippets only
  - Text in open clinical notes currently excluded
  - To consider: Radiology reports

### 2.3 General Guidelines for Disambiguation  
- Prefer anatomical region names over planning structure names unless unambiguous (e.g., “PTV_LUL” → left upper lobe).  
- If multiple regions appear (e.g., “oropharynx + bilateral neck”), extract each region separately.  

---

## 3. Mapping to CDM

**What should the NLP pipeline output?**  
Radiotherapy procedures as **Procedure Occurrence** (radiotherapy procedure concepts). For region extraction, create an **Observation** record documenting the anatomical target as a concept. Laterality should be applied as an additional modifier to the relevant procedure occurrence.

**Structured Output Format:**  

```json
{
    "observation": {
        "person_id": 1234,
        "observation_concept_id": 4165732,        // 4190005 (body site), 4240671 (body organ) - any child code thereof
        "observation_date": "2025-11-13",
        "observation_source_value": "ph2 prostate bed",
        "observation_event_id": 999,
        "obs_event_field_concept_id": 1147082     // procedure_occurrence.procedure_occurrence_id - this is applied as a modifier of radiotherapy procedure
    }
}
```