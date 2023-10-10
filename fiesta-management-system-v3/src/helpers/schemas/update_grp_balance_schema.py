UpdateGrpBalanceSchema = {
    "type": "object",
    "properties": {
        "grp_id": {"type": "integer"},
        "amount": {"type": "integer", "minimum": 1},
    },
    "required": ["grp_id", "amount"],
}