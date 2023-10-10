BalanceSchema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "balance": {"type": "integer"},
        "grp_id": {"type": "integer"},
    },
    "required": ["id", "balance", "grp_id"],
}
