import pandas as pd
import requests

contents_1 = pd.read_csv("https://pythonhow.com/data/sampledata.txt")
contents_2 = pd.read_csv("http://pythonhow.com/data/sampledata_x_2.txt")
contents = pd.concat([contents_1, contents_2])
# print(contents_1)
# print(contents_2)
# print(contents)

contents.to_csv("data.txt", index=None)
