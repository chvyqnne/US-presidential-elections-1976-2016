# Final Project Problem 4
# Cheyanne Cabang & Ricardo Sauerbrey

import pandas
import csv
import matplotlib.pyplot as plt


df = pandas.read_csv("1976-2016-president.csv")  # Import the file to Python


def fl_repvotes():
    """
    Florida Republican Votes from 1976-2016
    """

    print("---Florida Votes Over Time 1976-2016 for the Republican Party--- \n")  # Title for Output

    with open("1976-2016-president.csv") as myfile:  # Open the CSV File
        myfile_reader = csv.reader(myfile)  # Read the CSV file
        state = "Florida"  # Criteria for State
        fl_rep_votes = []  # Variable to store output

        for row in myfile_reader:
            if row[1] == state and row[8] == "republican":  # Values to Search for
                repvotes = row[10]
                year = row[0]
                print(row[1], "in", row[0], "had", row[10], "votes for the Republican party.")  # Desired Output Layout
                fl_rep_votes.append([year, repvotes])  # Appending each output to the list

        return fl_rep_votes


def fl_demvotes():
    """
    Florida Democrat Votes from 1976-2016
    """

    print("---Florida Votes Over Time 1976-2016 for the Democratic Party--- \n")  # Title for Output

    with open("1976-2016-president.csv") as myfile:  # Open the CSV File
        myfile_reader = csv.reader(myfile)  # Read the CSV file
        state = "Florida"  # Criteria for State
        fl_dem_votes = []  # Variable to store output

        for row in myfile_reader:
            demvotes = row[10]
            if row[1] == state and row[8] == "democrat":  # Values to Search for
                print(row[1], "in", row[0], "had", demvotes, "votes for the Democratic party.")  # Desired Output Layout
                fl_dem_votes.append(demvotes)  # Appending each output to the list

        return fl_dem_votes

# print("--republican votes:", fl_rep_votes, "\n--democrat votes:", fl_dem_votes)


def florida_votes_plot():
    """
    Plots Florida Republican votes from 1976-2016
    """

    data = fl_repvotes()
    year = df["year"]
    plt.plot(year, data, color="r")
    plt.title("Florida Votes Over Time 1976-2016 for the Republican Party")
    plt.xlabel("Year")
    plt.ylabel("Votes")
    return plt.show()

florida_votes_plot()