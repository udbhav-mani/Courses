import string

with open("countries_clean.txt", "r") as file:
    countries = file.read().split()

checklist = ["Portugal", "Germany", "Munster", "Spain"]
checklist = [country for country in checklist if country in countries]
print(checklist)