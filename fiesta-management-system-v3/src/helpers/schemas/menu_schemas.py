MenuSchema = {
    "type": "object",
    "properties": {
        "menu_id": {"type": "integer"},
        "date": {"type": "string", "format": "date-time"},
        "items": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["date", "items"],
}
UpdateItemSchema = {
    "type": "object",
    "properties": {
        "old_item": {"type": "string", "pattern": r"[a-zA-Z ]+"},
        "new_item": {"type": "string", "pattern": r"[a-zA-Z ]+"},
    },
    "required": ["old_item", "new_item"],
}
UpdateSchema = {
    "type": "object",
    "properties": {
        "menu_id": {"type": "integer"},
        "status": {
            "type": "string",
            "enum": ["pending", "published", "not published", "rejected", "discarded"],
        },
        "comments": {"type": "string"},
    },
    "required": ["menu_id", "status"],
}
