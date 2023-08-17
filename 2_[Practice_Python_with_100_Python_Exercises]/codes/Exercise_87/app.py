import string

with open("countries_clean.txt", "r") as file:
    countries = file.read().strip().split("\n")

checklist = ["Portugal", "Germany", "Spain"]
countries = countries + checklist
countries.sort()
# checklist = [country for country in checklist if country in countries]
print(countries)
with open("countries_fixed.txt", "w") as file:
    for country in countries:
        file.write(country + "\n")
