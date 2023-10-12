import json


queries = None
rbac = None
prompts = None
error_response = {
    "error": {"code": "", "message": ""},
    "status": "failure",
}

with open("data.json", "r") as file:
    data = json.load(file)
    queries = data["queries"]
    rbac = data["rbac"]
    prompts = data["prompts"]
