# MedspaCy & spaCy configurations

## Tokenization Strategy

Clinical text contains irregular punctuation, shorthand, unit expressions, and domain-specific notation that do not align well with typical tokenization behaviour. Tumour staging, abbreviations, units, measurements, genomic variants, and clinical shorthand all introduce patterns where:

* Punctuation can be meaningful, not merely syntactic
* Slash-delimited expressions contain multiple kinds of information
* Capitalisation and domain-specific abbreviations should remain joined

To support a consistent rule-based and matcher-based NLP pipeline, this project uses a two-phase tokenization strategy:

1. Overly enthusiastic initial splitting to avoid missed matches
2. Targeted reassembly of clinically meaningful multi-token units

All matcher rules in this catalogue assume this tokenisation strategy has been applied.


*Phase 1 — Brutal Splitting*

In the first pass, we deliberately over-split the text on characters that often obstruct lightweight NLP (such as slashes, periods, commas, parentheses)

*Phase 2 — Selective Reassembly*

After splitting, we recombine specific patterns that logically belong together, so that matcher patterns can work on semantically meaningful units (decimals & scientific notation, dates, times, units)

## ValueExtractor

ValueExtractor provides a utility class to wrap spaCy’s Matcher for the identification of text spans corresponding to specific clinical entities of the form `[label] [value]`. Extracting a usable `value` applies logic to match numeric (or literal) values within the overall labelled span.

Its purpose is to identify an entity defined by the label AND extract the value tied to it, using separate matchers.

It provides a uniform interface for:
* running a spaCy matcher
* filtering overlapping matches
* merging matched spans
* setting custom token-level flags (e.g., tok._.ecog = True)

To do this, requires creating patterns for:
* `token_patterns` tell the system how to find the overall span
* `value_patterns` tell the system how to extract the numeric or alphanumeric score inside the matched span
* `norm_patterns` (optional) normalise variant forms into a canonical label string.
* `exclusion_patterns` (optional) exclude common false-positive matches

*Example:*
* It identifies the *phrase* “PG-SGA score (3b)” as a single span via token_patterns.
* It finds the *value* "3b" inside that span via value_patterns.
* It merges the whole span to one token.
* It attaches attributes:
    * tok._.pgsga = True
    * tok._.pgsga_value = 3 OR "3b" (depending on normalisation logic)
    * If entity_label is set, it creates a clinical entity.