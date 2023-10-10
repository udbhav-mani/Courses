MenuSchema = {
    "type": "object",
    "properties": {
        "menu_id": {"type": "integer"},
        "date": {"type": "string", "format": "date-time"},
        "items": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["date", "items"],
}