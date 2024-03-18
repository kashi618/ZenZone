import csv
import numpy as np
from matplotlib import pyplot as plt
import statistics
from statistics import mode

def graphFromCSV():
    # Add graph labels
    plt.xlabel("Time (hours)")
    plt.ylabel("General Emotional State")

    # Add line of best fit to graph
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
    # Add data points on graph
    plt.scatter(x,y) 
    # Show graph
    plt.show()

def importDataFromCSV():
    # Opens up CSV for reading
    csv_file = open("testDataset.csv","r")
    csv_reader = csv.reader(csv_file)
    
    # Skips first line on csv, as it is the title
    next(csv_reader)

    # Initialize variables
    y = []
    x = [1,2,3,4,5,6,7,8,9,10]
    emotions = []

    # This takes in the values from the CSV, and adds them to a list 
    for row in csv_reader:
        if row[0] == "Happy":
            y.append(int(row[1]))
            emotions.append("Happy")
        elif row[0] == "Neutral":
            y.append(0)
            emotions.append("Neutral")
        elif row[0] == "Sad":
            y.append(-abs(int(row[1])))
            emotions.append("Sad")
    
    # Close CSV file and return X and Y values
    csv_file.close()
    return x,y,emotions

def main(x,y,avgEmotions):
    print("Hi, Welcome to ZenZone :)")
    
    if input("Have you generated a CSV dataset with the microbit yet? (Y,N)\n").lower() == "y":
        print("Which one of these functions do you want to see?")
        print("(1) Graph of general emotional state")
        print("(2) Average emotional state (as a number)")
        print("(3) Most frequent emotion felt")
        
        if input() == "1":
            graphFromCSV()
            
        elif input() == "2":
            for i in range(len(y)-1):
                sumOfNum += y[i]
                mean = sumOfNum / len(y)
            print(mean)
        elif input() == "3":
            print(mode(emotions))
    else:
        print("Come back when you have :)")
    

x,y,emotions = importDataFromCSV()


main(x,y,emotions)


