<p align="center">
  <a href="https://github.com/AustralianCancerDataNetwork/onco_nlp_resources/actions/workflows/deploy.yml">
    <img src="https://github.com/AustralianCancerDataNetwork/onco_nlp_resources/actions/workflows/deploy.yml/badge.svg" alt="Deploy Status">
  </a>

  <a href="https://australiancancerdatanetwork.github.io/onco_nlp_resources/">
    <img src="https://img.shields.io/badge/docs-github%20pages-blue.svg" alt="Documentation">
  </a>
</p>


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
