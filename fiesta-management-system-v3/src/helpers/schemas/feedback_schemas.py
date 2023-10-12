FeedbackSchema = {
    "type": "object",
    "properties": {
        "feedback": {"type": "number", "minimum": 0, "maximum": 5},
        "criteria": {"type": "string", "pattern": r"[a-zA-z ]+"},
        "comments": {"type": "string"},
    },
    "required": ["feedback", "criteria", "comments"],
}
PlainFeedbackSchema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "cr_id": {"type": "integer", "minimum": 1},
            "feedback": {"type": "number", "minimum": 0, "maximum": 5},
            "comments": {"type": "string", "pattern": r"[a-zA-z ]+"},
        },
        "required": ["cr_id", "feedback", "comments"],
    },
}
