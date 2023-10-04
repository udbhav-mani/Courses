import json

from src.helpers.entry_page import ChoiceDisplayer
from src.utils import config

if __name__ == "__main__":
    with open(
        r"C:\Users\umani\Desktop\Courses\fiesta-management-system\data.json", "r"
    ) as file:
        data = json.load(file)
        config.prompts = data["menu_choices"]
        config.queries = data["queries"]
    entry = ChoiceDisplayer()
    entry.entry()
