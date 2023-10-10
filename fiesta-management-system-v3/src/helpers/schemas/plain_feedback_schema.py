PlainFeedbackSchema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "cr_id": {"type": "integer"},
            "feedback": {"type": "number", "minimum": 0, "exclusiveMaximum": 6},
            "comments": {"type": "string"},
        },
        "required": ["cr_id", "feedback", "comments"],
    },
}
