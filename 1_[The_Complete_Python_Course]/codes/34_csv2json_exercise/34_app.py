# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:

import json

csv_file = open("csv_file.txt", "r")
csv_file = [file.strip().split(",") for file in csv_file]
club_list = list()
for team in csv_file:
    team_name = team[0]
    team_city = team[1]
    team_country = team[2]

    club_list.append({"club": team_name, "country": team_country, "city": team_city})


json_file = open("json_file.txt", "w")
json.dump(club_list, json_file)
json_file.close()

# print(json_file)
