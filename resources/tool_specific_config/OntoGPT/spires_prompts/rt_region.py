
system_prompt = """
Act as a clinician with a specialist practice in radiation oncology.
You are are preparing to meet with a new patient and reviewing their clinical record to understand their treatment history.
You are specifically interested in identifying any radiotherapy regions that have been treated previously and are looking at the labelled radiotherapy region.
Please extract all radiotherapy regions mentioned in the text, including any abbreviations or synonyms. 
Do not add any details that are not explicitly mentioned in the input text.
Do not include any preamble or explanation of reasoning.
"""

examples = {
    "wbrt": {
        "label": "wbrt",
        "location": "brain",
        "body_site": ["brain"],
        "relative_location": "whole"
    },
    "l1": {
        "label": "l1",
        "location": "l1 vertebra",
        "body_site": ["spine"],
        "spinal_region": [{"concept_name": "lumbar"}]
    },
    "t2": {
        "label": "t2",
        "location": "t2 vertebra",
        "body_site": ["spine"],
        "spinal_region": [{"concept_name": "thoracic"}]
    },
    "lt cheek": {
        "label": "lt cheek",
        "location": "cheek",
        "body_site": ["cheek"],
        "laterality": {"concept_name": "left"}
    },
    "tip of nose": {
        "label": "tip of nose",
        "location": "nose",
        "body_site": ["nose"],
        "relative_location": "tip",
    },
    "prostate":   {
        "label": "prostate",
        "location": "prostate",
        "body_site": ["prostate"]
    },
    "prox sv":   {
        "label": "prox sv",
        "location": "seminal vesicles",
        "body_site": ["seminal vesicles"],
        "relative_location": "proximal"
    },
    "sv":   {
        "label": "sv",
        "location": "seminal vesicles",
        "body_site": ["seminal vesicles"]
    },
    "(r) breast boost": {
        "label": "(r) breast",
        "location": "breast",
        "body_site": ["breast"],        
        "laterality": {"concept_name": "right"},
        "technique": "boost"
    },
    "ph2 prostate bed": {
        "label": "ph2 prostate bed",
        "location": "prostate",
        "body_site": ["prostate"],
        "relative_location": "bed",
        "technique": "ph2"
    },
    "scf": {
        "label": "scf",
        "location": "supraclavicular fossa",
        "body_site": ["supraclavicular fossa"],
    },
}
