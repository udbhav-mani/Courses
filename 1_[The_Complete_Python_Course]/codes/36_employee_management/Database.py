import json


class Database:
    def __init__(self, filename="data.json"):
        self.filename = filename

    def update_database(self, contents):
        with open(self.filename, "w") as file:
            json.dump(contents, file, indent=2)

    def fetch_data(self):
        with open(self.filename, "r") as file:
            contents = json.load(file)

        return contents
