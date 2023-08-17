import pandas as pd
import pylab as plt


contents = pd.read_csv("https://pythonhow.com/data/sampledata.txt")
contents.plot(kind="scatter", x="x", y="y")
# contents.plot(kind="bar", x="x", y="y", color="red")
plt.show()
