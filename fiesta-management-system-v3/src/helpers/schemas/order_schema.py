OrderSchema = {
    "type": "object",
    "properties": {
        "user_id": {"type": "integer", "minimum": 1},
        "amount": {"type": "number", "minimum": 0},
    },
    "required": ["user_id", "amount"],
}
