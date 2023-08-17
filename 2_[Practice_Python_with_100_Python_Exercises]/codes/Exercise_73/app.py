import pandas as pd

contents = pd.read_csv("https://pythonhow.com/data/sampledata.txt")
contents = contents * 2
contents.to_csv("data.txt", index=None)
print(contents)
