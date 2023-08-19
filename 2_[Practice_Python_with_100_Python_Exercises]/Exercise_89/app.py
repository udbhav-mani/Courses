import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute("select * from countries where area >= 2000000")
countries = [country[1] for country in cursor.fetchall()]

for country in countries:
    print(country)
connection.close()
