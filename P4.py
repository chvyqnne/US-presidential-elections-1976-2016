# Final Project Problem 4
# Cheyanne Cabang & Ricardo Sauerbrey

import pandas
import csv

file = pandas.read_csv("1976-2016-president.csv")  # Import the file to Python


def fl_repvotes():
    print("---Florida Votes Over Time 1976-2016 for the Republican Party--- \n")  # Title for Output
    with open("1976-2016-president.csv") as myfile:  # Open the CSV File
        myfile_reader = csv.reader(myfile)  # Read the CSV file
        state = "Florida"  # Criteria for State
        fl_rep_votes = []  # Variable to store output
        for row in myfile_reader:
            if row[1] == state and row[8] == "republican":  # Values to Search for
                repvotes = row[10]
                print(row[1], "in", row[0], "had", row[10], "votes for the Republican party.")  # Desired Output Layout
                fl_rep_votes.append(repvotes)  # Appending each output to the list


def fl_demvotes():
    print("---Florida Votes Over Time 1976-2016 for the Democratic Party--- \n")  # Title for Output
    with open("1976-2016-president.csv") as myfile:  # Open the CSV File
        myfile_reader = csv.reader(myfile)  # Read the CSV file
        state = "Florida"  # Criteria for State
        fl_dem_votes = []  # Variable to store output
        for row in myfile_reader:
            demvotes = row[10]
            if row[1] == state and row[8] == "democrat":  # Values to Search for
                print(row[1], "in", row[0], "had", row[10], "votes for the Democratic party.")  # Desired Output Layout
                fl_dem_votes.append(demvotes)  # Appending each output to the list

# print("--republican votes:", fl_rep_votes, "\n--democrat votes:", fl_dem_votes)


fl_repvotes(), fl_demvotes()
