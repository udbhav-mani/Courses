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
