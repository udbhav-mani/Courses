UpdateUserBalanceSchema = {
    "type": "object",
    "properties": {
        "user_id": {"type": "integer"},
        "amount": {"type": "integer", "minimum": 1},
    },
    "required": ["user_id", "amount"],
}
