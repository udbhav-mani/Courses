import pandas as pd

data = pd.read_csv("countries_by_area.txt")
data["density"] = data["population_2013"] / data["area_sqkm"]
data = data.sort_values(by=["density"], ascending=False)

for index, data in data[:5].iterrows():  # iterates over it as index, series pair
    print(data["country"])
