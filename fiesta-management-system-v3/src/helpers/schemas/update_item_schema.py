UpdateItemSchema = {
    "type": "object",
    "properties": {"old_item": {"type": "string"}, "new_item": {"type": "string"}},
    "required": ["old_item", "new_item"],
}
