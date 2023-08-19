import sqlite3
import pandas as pd

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute("select * from countries where area >= 2000000")
countries = [country for country in cursor.fetchall()]

connection.close()
print(countries)
df = pd.DataFrame(countries, columns=["rank", "country", "area", "population"])

# print(df)
df.to_csv("data.csv", index=None)
# with open("data.csv", "w") as file:
