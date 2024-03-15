import csv
import numpy as np
from matplotlib import pyplot as plt

csv_file = open("testDataset.csv","r")
csv_reader = csv.reader(csv_file)
next(csv_reader)

y = []
x = [1,2,3,4,5,6,7,8,9,10]

for row in csv_reader:
    if row[0] == "Happy":
        y.append(int(row[1]))
    elif row[0] == "Neutral":
        y.append(0)
    elif row[0] == "Sad":
        y.append(-abs(int(row[1])))


plt.xlabel("Time (hours)")
plt.ylabel("General Emotional State")

# Add line of best fit to graph
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
# Add data points on graph
plt.scatter(x,y) 
# Show graph
plt.show()

csv_file.close()