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