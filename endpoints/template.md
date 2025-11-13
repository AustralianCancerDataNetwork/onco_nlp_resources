# Endpoint Name 
--- 
## 1. Endpoint Definition 
**Description:** 
> *Replace this with a concise explanation of what the clinical endpoint captures, why it matters, and where it typically appears (structured fields, clinical notes, pathology reports, treatment plans, etc.).* 

**Relevant Background & Links:** 
> *Add key clinical references, guideline citations, coding manuals, or other external standards.* 

**Cancer Domains:** 
> *List the cancer domains this endpoint applies to (e.g., Lung, Colorectal, Head & Neck, All).* 

**Endpoint Type:** 
> *Categorical / Numeric / Text extraction / EAV / Entity Linking / Temporal Relationship (select one or multiple).* 

**Endpoint Status:** 
| Assessment | Details | 
|-----------|---------| 
| **Feasibility** | *Comment on feasibility: how commonly expressed? how ambiguous? how consistent across sites?* | 
| **Priority** | *Why this endpoint is clinically or analytically important; when it is needed.* | 
| **Maturity / Current State** | *Describe prototypes, heuristics, notebooks, partial implementations, or upstream dependencies.* | 
| **Shareability** | *How much site-specific tuning is required? How portable is this extraction target?* | 

--- 

## 2. Examples 
### 2.1 Positive Examples 

> *Provide representative sentences or fragments from clinical notes that clearly express the endpoint.* 
> - *Example positive phrasing 1* 
> - *Example positive phrasing 2* 
> - *Example positive phrasing 3* 

### 2.2 Negative / Exclusions

> *Provide examples that appear related but should not be extracted, or cases that require explicit handling.* 
> - *Ambiguous or misleading example 1* > - *Ambiguous example 2* 
> - *Narrative text that should not be mapped to the endpoint* 

### 2.3 General Guidelines for Disambiguation 
> *Document rules-of-thumb for resolving ambiguous expressions, ranges, qualifiers, negations, or conflicting statements.* 
> - *Guideline example (e.g., choose higher value in ranges)* 
> - *Guideline for resolving multi-sentence context* 
> - *Guideline for ignoring hypothetical statements* 

--- 

## 3. Mapping to CDM 

**What should the NLP pipeline output?** 
> *Describe the required OMOP CDM representation: Measurement, Observation, Condition, Drug Exposure, Episode, etc.* 
**Structured Output Format:** 
> *Replace this JSON block with the expected structure for this endpoint (including CDM concept IDs).*
json
{
    "measurement": {
        "person_id": "...",
        "measurement_concept_id": "...",
        "measurement_date": "...",
        "value_as_number": "...",
        "value_as_concept_id": "...",
        "value_source_value": "..."
    }
}


---

### 4. Existing Work

**Current Solutions or Prototypes:**

> Demo binder: 

**Implementations in Use:**

> Include performance evaluations if available

---

## 5. Proposed Approach

> (complete as relevant/appropriate)

**Rule-based / Heuristic Approach**

> * List key patterns or features
> * Example regex/patterns
> * Expected performance / challenges

**Zero-shot Approach**

> * General specifications for structured prompting & extraction

**Custom / Fine-tuned Apprach**

> * Complexity justification
> * Validation Considerations
