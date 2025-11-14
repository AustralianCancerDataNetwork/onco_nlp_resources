# Collaborative Prompt Library Guidelines  
_A cross-site approach for reliable, versioned, and reproducible prompt engineering_

Goal: set up and maintain a **shared prompt library**, ensuring that:

- **Prompts are reproducible** across teams and compute environments  
- **Outputs follow a common schema**, so downstream pipelines (ETL, dashboards, validation interfaces) can rely on them  
- **Methods can be peer-reviewed**, improved, and benchmarked transparently  
- **Tools and patterns can be re-used** across cancer domains  
- **Version control tracks lineage** of every change to prompt logic or output structure  

This collaborative approach lets teams contribute LLM-based development into a shared ecosystem.

---

## How the Prompt Library Works

**[Prompt-O](https://github.com/AustralianCancerDataNetwork/prompt-o)** is a lightweight linkML-based toolchain with a few simple wrapper tools for common use-cases.

Each extraction target (e.g., *conditions*, *performance status*, *radiotherapy region*) is represented using a **[LinkML schema](https://linkml.io/linkml/schemas/)**

LinkML provides:

- A clear **data contract**
- Strong typing (e.g., enums, ranges, nested objects)
- Ability to generate **pydantic models** via `gen-pydantic`
- Portable schemas that can be reused (and extended) outside this project  
- Validation of LLM outputs  
- Automatic JSON conversion  
- Type-safe integration with downstream python code  

> These schemas define *what* an LLM must return.  
> They do **not** dictate *how* extraction is done.

Prompts themselves are authored and stored in plain **YAML** files.

Each prompt definition file contains:

- `system`: instructions to the model  
- `instruction`: task description  
- `output_model`: the LinkML/Pydantic model to use  
- `examples`: zero-shot, few-shot, or scenario-based examples  

---

### Recommended Workflow for Collaborators

1. Identify an [endpoint](../endpoints/) e.g. ECOG, radiotherapy region, variant of interest
2. Define or update the LinkML schema, ensuring output fields match analytic needs 
    - The schema definitions can be submitted to the [OntoGPT tool-specific configuration folder](../../resources/tool_specific_config/OntoGPT/templates/)
3. Generate the Pydantic model
4. Create a new prompt file
5. Write or refine the system prompt + examples, includin few-shot examples whenever possible
6. Validate prompts
7. Submit draft to [prompt library](../../resources/prompt_library/) for network validation & iteration

_Note: Detailed instructions for steps 3 through 6 can be found at_ https://github.com/AustralianCancerDataNetwork/prompt-o