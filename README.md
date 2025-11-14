# Oncology NLP Endpoint Catalogue
A Collaborative Resource for Practical, Shareable Clinical NLP Tools

### Why This Catalogue Exists

Creating a shared place to:

* consolidate oncology-specific extraction targets
* identify simple, robust solutions
* map community expertise
* share ready-to-use notebooks, heuristics, regexes, and workflows
* avoid duplicative effort across sites

---

# Introduction

For now, this is just holding a list of files and statuses - to add more context later

## Endpoints

[Performance Status](./documentation/endpoints/performance_status.md)
[Radiotherapy Regions](./documentation/endpoints/radiotherapy_regions.md)


## Tasks

[Tokenization](./documentation/task_specific/tokenization.md)
[Prompting](./documentation/task_specific/prompting.md)

## Tools

[medspaCy](./documentation/tool_specific/medspaCy.md)

---

| Endpoint                       | Feasibility | Priority | Maturity | Shareability | Link                                        |
| ------------------------------ | ----------- | -------- | -------- | ------------ | ------------------------------------------- |
| **Performance Status (ECOG)**  | High        | High     | High     | High         | [Performance Status](./documentation/endpoints/performance_status.md) |
| **Smoking History**            | High        | Medium   | Medium   | Medium       | [Smoking History](./documentation/endpoints/smoking.md)       |
| **Actionable Genomic Variant** | Low–Medium  | High     | Low      | Medium       | [Genomic Variant](./documentation/endpoints/genomic_variants.md)       |
| **Oral Chemotherapy Use**      | Medium      | Medium   | Low      | Low–Medium   | [Oral Chemotherapy](./documentation/endpoints/oral_chemo.md)          |
| **Radiotherapy Site / Region** | High        | Medium   | Medium   | High         | [Radiotherapy Region](./documentation/endpoints/radiotherapy_regions.md)         |

---

## Open Questions
* How do we best curate all the mapping targets in a single location for maintainability?
* As a start, this is mostly a collection of pointers, notes, conventions 
    * need a straightforward way to provide minimal working examples to support their use
* For logical units of work it would be better to apply in-code documentation
    * at this point the structure is quite loose and therefore the most sensible location for this isn't clear 
    * strategic decision-making required
* medspacy customisations for tokenisation / sectionising are sufficiently nuanced to not be just `config files`
    * create registerable spacy language with these customisations - where will it live?
    * value-extractor + label-extractor classes as PR?
