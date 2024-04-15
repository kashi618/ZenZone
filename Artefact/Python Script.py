import csv
import numpy as np
from matplotlib import pyplot as plt
from statistics import mode

def graphFromCSV(x,y):
    # Add graph labels
    plt.xlabel("Time (hours)")
    plt.ylabel("General Mood Level")

    # Add line of best fit to graph
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
    # Add data points on graph
    plt.scatter(x,y) 
    # Show graph
    plt.show()

def importDataFromCSV():
    # Opens up CSV for reading
    csv_file = open("Microbit/testDataset.csv","r")
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

def main(x,y,emotions):
    sumOfNum = 0
    generalEmotionalState = 0
    print("\n\n\nHi, Welcome to ZenZone :)")
    
    if input("Have you generated a CSV dataset with the microbit yet? (Y,N)\n").lower() == "y":
        while True:
            print("\nWhich one of these functions do you want to see?")
            print("(1) Graph of general emotional state")
            print("(2) General mood")
            print("(3) Most frequent emotion felt")
            print("(4) What if Questions")
            userInput = input()

            if userInput == "1":
                graphFromCSV(x,y)
                
                if input("Would you like to continue? (Y/N)\n").lower() == "n":
                    print("Thank you")
                    exit()
            
            elif userInput == "2":
                # Find the general emotional state, by finding the average of the emotions felt (Returns a number)
                for i in range(len(y)-1):
                    sumOfNum += y[i]
                    mean = sumOfNum / len(y)
                mean = generalEmotionalState
                
                # Using the value of the general emotional state, 
                # It tells the user if they are sad(<0), neutral(=0), happy(<0)
                if generalEmotionalState < 0:
                    print("\nYour average emotion is Sad :(")
                elif generalEmotionalState == 0:
                    print("\nYour average emotion is neutral :|")
                elif generalEmotionalState > 0:
                    print("\nYour average emotion is happy :)")
                
                # Asks user if they want to continue using the program
                if input("Would you like to continue? (Y/N)").lower() == "n":
                    print("Thank you")
                    exit()
            
            if userInput == "3":
                # Using statistics module, find the most frequent emotion felt throughout the day
                print("\n"+mode(emotions))

                #Asks user if they want to continue using the program
                if input("Would you like to continue? (Y/N)").lower() == "n":
                    print("Thank you")
                    exit()
            
            if userInput == "4":
                print("\nWhat if question 1")
                print("How does my mood vary thoughout the day?")
                print("")
                
                # Reuses code from line 77, to predice mood
                if generalEmotionalState > 0:
                    print("Your predicted mood throughout the day will be generally happy")
                elif generalEmotionalState == 0:
                    print("Your predicted mood throughout the day will be generally neutral")
                elif generalEmotionalState < 0:
                    print("Your predicted mood throughout the day will be generally sad")
                
                input("Show next question? (Y/N)")
                
                print("\nWhat if question 2")
                print("If I was very sad in the morning, how will it affect my general emotional state?")
                print("")
                print("To tackle this question, we start by using the dataset collected from the user earlier as a control.")
                print("From this dataset, we change the emotions felt in the morning to sad")
                print("We then graph this new dataset, and find out the general emotional state")
                
                if input("Show graph? (Y/N)").lower() == "y":
                    # Reuses code from line6, to graph general emotional state
                    x = [1,2,3,4,5,6,7,8,9,10]
                    y = [-5,-5,-5,-5,1,0,3,1,5,3]
                    plt.xlabel("Time (hours)")
                    plt.ylabel("General Mood Level")
                    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
                    plt.scatter(x,y) 
                    plt.show()
                
                print("\nFrom this graph, lets predict the general emotional state")
                for i in range(len(y)-1): # Reuses code from line 70, to find general emotional state
                    sumOfNum += y[i]
                    mean = sumOfNum / len(y)
                
                print("The general emotional state is:",mean)
                print("Which gives us slightly sad")
                
                if input("\nWould you like to continue? (Y/N)").lower() == "n":
                    print("Thank you")
                    exit()
            
    else:
        print("Please generate the dataset with the microbit.")

# Sets up variables for use
x,y,emotions = importDataFromCSV()
# Calls main function of program
main(x,y,emotions)


