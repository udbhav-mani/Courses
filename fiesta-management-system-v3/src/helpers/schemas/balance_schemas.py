BalanceSchema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer", "minimum": 1},
        "balance": {"type": "number", "minimum": 1},
        "grp_id": {"type": "integer", "minimum": 1},
    },
    "required": ["id", "balance", "grp_id"],
}
UpdateGrpBalanceSchema = {
    "type": "object",
    "properties": {
        "grp_id": {"type": "integer", "minimum": 1},
        "amount": {"type": "number", "minimum": 0},
    },
    "required": ["grp_id", "amount"],
}
UpdateUserBalanceSchema = {
    "type": "object",
    "properties": {
        "user_id": {"type": "integer"},
        "amount": {"type": "integer", "minimum": 1},
    },
    "required": ["user_id", "amount"],
}
