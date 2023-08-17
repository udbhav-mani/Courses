import pandas as pd

data = pd.read_csv("countries_by_area.txt")
data.sort_values(by=["population_2013"])
print(data)
