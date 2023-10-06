import json


queries = None
error_response = {
    "error": {"code": "", "message": ""},
    "status": "failure",
}

with open("data.json", "r") as file:
    data = json.load(file)
    queries = data["queries"]
