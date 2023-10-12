CriteriaSchema = {
    "type": "object",
    "properties": {
        "criteria": {
            "type": "array",
            "items": {"type": "string", "pattern": r"[a-zA-z ]+"},
        }
    },
    "required": ["criteria"],
}

CriteriaResponseSchema = {
    "type": "object",
    "properties": {
        "criteria": {"type": "string", "pattern": r"[a-zA-z ]+"},
        "cr_id": {"type": "integer", "minimum": 1},
    },
    "required": ["criteria", "cr_id"],
}
