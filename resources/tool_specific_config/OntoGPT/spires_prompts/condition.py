
system_prompt = """
Act as a medical data entry specialist.
You are reading notes from a clinical record that contains information about a patient's current and historical diagnoses, as well as relevant family history.
You have been asked to extract all conditions mentioned in the text, noting its status (e.g., active, resolved, suspected, etc.) and whether it was specifically the patient's diagnosis or belongs to a family member.
Please extract all conditions mentioned in the text, including any abbreviations or synonyms. 
Do not add any details that are not explicitly mentioned in the input text.
You are not a clinician, so do not infer conditions based on symptoms or other indirect information. Code explicitly mentioned conditions only.
Do not include any preamble or explanation of reasoning.
"""

examples = {
    "This 72-year-old male has a new diagnosis of prostate cancer": {
        "conditions": [
            {
                "label": "prostate cancer",
                "verbatim_name": "prostate cancer",
                "codable_name": "prostate cancer",
                "who_diagnosed": "subject",
                "status": "active",
                "is_negated": False
            }
        ]
    },
    "Her mother had early-onset colon cancer and her sister has a history of melanoma.": {
        "conditions": [
            {
                "label": "colon cancerr",
                "verbatim_name": "colon cancer",
                "codable_name": "colorectal cancer",
                "who_diagnosed": "family",
                "is_negated": False
            },
            {
                "label": "melanoma",
                "verbatim_name": "melanoma",
                "codable_name": "melanoma",
                "who_diagnosed": "family",
                "is_negated": False
            },
        ]
    },
    "The patient was treated for mild rheumatoid arthritis in her 30s, which has been in remission for over a decade.":{
        "conditions":[
            {
                "label": "rheumatoid arthritis",
                "verbatim_name": "rheumatoid arthritis",
                "codable_name": "rheumatoid arthritis",
                "who_diagnosed": "subject",
                "severity": {"concept_name": "mild"},
                "status": "inactive",
                "is_negated": False
            },
        ]
    },
    "No family history of diabetes.":{
        "conditions":[
            {
                "label": "diabetes",
                "verbatim_name": "diabetes",
                "codable_name": "diabetes",
                "who_diagnosed": "family",
                "is_negated": True
            }
        ]
    }
}

