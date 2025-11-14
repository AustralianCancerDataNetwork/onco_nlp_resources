# Prompt Curation

## Collaborative Prompt Library  
_A cross-site approach for reliable, versioned, and reproducible prompt engineering_

/// attention | Goal 
Set up and maintain a **shared prompt library**
- **Prompts are reproducible** across teams and compute environments  
- **Outputs follow a common schema**, so downstream pipelines (ETL, dashboards, validation interfaces) can rely on them  
- **Methods can be peer-reviewed**, improved, and benchmarked transparently  
- **Tools and patterns can be re-used** across cancer domains  
- **Version control tracks lineage** of every change to prompt logic or output structure  
///

This collaborative approach lets teams contribute LLM-based development into a shared ecosystem.

---

## Prompt Library Operations

**[Prompt-O](https://github.com/AustralianCancerDataNetwork/prompt-o)** is a lightweight linkML-based toolchain with a few simple wrapper tools for common use-cases.

Each extraction target (e.g., *conditions*, *performance status*, *radiotherapy region*) is represented using a **[LinkML schema](https://linkml.io/linkml/schemas/)**

/// attention | LinkML provides 
- A clear **data contract**
- Strong typing (e.g., enums, ranges, nested objects)
- Ability to generate **pydantic models** via `gen-pydantic`
- Portable schemas that can be reused (and extended) outside this project  
- Validation of LLM outputs  
- Automatic JSON conversion  
- Type-safe integration with downstream python code  
///

/// tip | Note
These schemas define *what* an LLM must return.  They do **not** dictate *how* extraction is done.
///

Prompts themselves are authored and stored in plain **YAML** files.

Each prompt definition file contains:

- `system`: instructions to the model  
- `instruction`: task description  
- `output_model`: the LinkML/Pydantic model to use (seeks tree_root class, or if not, defaults to camel case version of the file name) 
- `examples`: zero-shot, few-shot, or scenario-based examples  

```yaml {title="Example prompt definition for few-shot task"}
name: oncology_condition_extraction
prompt_type: few_shot
system: >
  Act as a medical data entry specialist.
  You are reading notes from a clinical record that contains ...
instruction: >
  Extract all conditions mentioned in the text...
output_model: condition_model

examples:
  - input: "This 72-year-old male has a new diagnosis of prostate cancer"
    output: |
      {"conditions": [{"label":"prostate cancer", "verbatim_name": "prostate cancer", "codable_name": "prostate cancer", "who_diagnosed": "subject", "status":"active", "is_negated": false}]}
```

```python {title="Snippet of related pydantic class for provided example (generated)"}

class WhoDiagnosed(str, Enum):
    family = "family"
    subject = "subject"
    unknown = "unknown"

class OMOPEnum(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'omop:convention'})
    concept_name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['OMOPEnum', 'ConditionDiagnosisSeverity']} })
    concept_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['OMOPEnum']} })

class ConditionDiagnosisSeverity(OMOPEnum):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'meaning': {'tag': 'meaning', 'value': 'concept_id'}},'from_schema': 'ohdsi:condition'})
    concept_name: Optional[ConditionDiagnosisSeverityEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['OMOPEnum', 'ConditionDiagnosisSeverity']} })
    concept_id: Optional[str] = Field(default=None, description="""concept_id for the enum label""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['OMOPEnum']} })

class Condition(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'ohdsi:condition'})
    label: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['OMOPHierarchy', 'Condition']} })
    verbatim_name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Condition']} })
    who_diagnosed: Optional[WhoDiagnosed] = Field(default='unknown', json_schema_extra = { "linkml_meta": {'domain_of': ['Condition'], 'ifabsent': 'string("unknown")'} })
    is_negated: Optional[bool] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Condition']} })
    severity: Optional[ConditionDiagnosisSeverity] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Condition']} })

```

---

## Recommended Workflow

1. Identify an [endpoint](../endpoints/endpoint_catalogue.md) e.g. ECOG, radiotherapy region, variant of interest
2. Define or update the LinkML schema, ensuring output fields match analytic needs 
    - The schema definitions can be submitted to the [OntoGPT tool-specific configuration folder]({{ github_base }}/resources/tool_specific_config/OntoGPT/templates/)
3. Generate the Pydantic model
4. Create a new prompt file
5. Write or refine the system prompt + examples, includin few-shot examples whenever possible
6. Validate prompts
7. Submit draft to [prompt library]({{ github_base }}/resources/tool_specific_config/OntoGPT/spires_prompts/) for network validation & iteration

_Note: Detailed instructions for steps 3 through 6 can be found at_ https://github.com/AustralianCancerDataNetwork/prompt-o