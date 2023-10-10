UpdateUserBalanceSchema = {
    "type": "object",
    "properties": {
        "user_id": {"type": "integer"},
        "amount": {"type": "integer", "minimum": 1},
    },
    "required": ["user_id", "amount"],
}

UpdateGrpBalanceSchema = {
    "type": "object",
    "properties": {
        "grp_id": {"type": "integer"},
        "amount": {"type": "integer", "minimum": 1},
    },
    "required": ["grp_id", "amount"],
}

# OrderSchema
OrderSchema = {
    "type": "object",
    "properties": {
        "user_id": {"type": "integer"},
        "amount": {"type": "integer", "minimum": 1},
    },
    "required": ["user_id", "amount"],
}

# MenuSchema
MenuSchema = {
    "type": "object",
    "properties": {
        "menu_id": {"type": "integer"},
        "date": {"type": "string", "format": "date-time"},
        "items": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["date", "items"],
}

# UpdateSchema
UpdateSchema = {
    "type": "object",
    "properties": {
        "menu_id": {"type": "integer"},
        "status": {
            "type": "string",
            "enum": [
                "pending",
                "published",
                "not published",
                "rejected",
            ],
        },
        "comments": {"type": "string"},
    },
    "required": ["menu_id", "status"],
}

# UserSchema
UserSchema = {
    "type": "object",
    "properties": {"username": {"type": "string"}, "password": {"type": "string"}},
    "required": ["username", "password"],
}

# BalanceSchema
BalanceSchema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "balance": {"type": "integer"},
        "grp_id": {"type": "integer"},
    },
    "required": ["id", "balance", "grp_id"],
}

# UpdateItemSchema
UpdateItemSchema = {
    "type": "object",
    "properties": {"old_item": {"type": "string"}, "new_item": {"type": "string"}},
    "required": ["old_item", "new_item"],
}

# CriteriaSchema
CriteriaSchema = {
    "type": "object",
    "properties": {"criteria": {"type": "array", "items": {"type": "string"}}},
    "required": ["criteria"],
}

# CriteriaResponseSchema
CriteriaResponseSchema = {
    "type": "object",
    "properties": {"criteria": {"type": "string"}, "cr_id": {"type": "integer"}},
    "required": ["criteria", "cr_id"],
}

# PlainFeedbackSchema
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

# FeedbackSchema
FeedbackSchema = {
    "type": "object",
    "properties": {
        "feedback": {"type": "number"},
        "criteria": {"type": "string"},
        "comments": {"type": "string"},
    },
    "required": ["feedback", "criteria", "comments"],
}
