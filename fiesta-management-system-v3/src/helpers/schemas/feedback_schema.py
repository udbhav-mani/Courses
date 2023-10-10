FeedbackSchema = {
    "type": "object",
    "properties": {
        "feedback": {"type": "number"},
        "criteria": {"type": "string"},
        "comments": {"type": "string"},
    },
    "required": ["feedback", "criteria", "comments"],
}
