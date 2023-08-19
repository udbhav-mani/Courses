import sqlite3
import pandas as pd

data_list = list()
new_countries = pd.read_csv("ten_more_countries.txt")
for index, data in new_countries.iterrows():
    data_list.append(
        {"id": data["ID"], "country": data["Country"], "area": data["Area"]}
    )

# print(data_list)

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
for data in data_list:
    cursor.execute(
        "INSERT INTO countries (id, country, area, population) VALUES (?,?,?, NULL)",
        (data["id"], data["country"], data["area"]),
    )


connection.commit()
connection.close()
# print(countries)
# df = pd.DataFrame(countries, columns=["rank", "country", "area", "population"])

# # print(df)
# df.to_csv("data.csv", index=None)
# # with open("data.csv", "w") as file:
