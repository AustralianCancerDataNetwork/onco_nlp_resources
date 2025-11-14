# MedspaCy & spaCy configurations

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