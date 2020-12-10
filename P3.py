# Final Project Question 3
# Cheyanne Cabang & Ricardo Sauerbrey

import pandas
import csv

file = pandas.read_csv("1976-2016-president.csv")  # Import the file to Python


def rep_states2012():
    """

    """
    print("---Top 5 Republican States with the Highest Supporting Rate in 2012--- \n")  # Title for Output

    with open("1976-2016-president.csv") as myfile:  # Open the CSV File
        rep_states_2012 = []  # Variable to store output
        year = "2012"  # Criteria for year
        myfile_reader = csv.reader(myfile)  # Read the CSV file
        for row in myfile_reader:
            if row[0] == year and row[8] == "republican" and float(row[14][:len(row[14]) - 1]) > 62.29:  # Values to Search for
                print(row[1], "with a supporting rate of", row[14])  # Desired Output Layout
                rep_states_2012.append(row[14])  # Appending each output to the list

        return rep_states_2012

rep_states2012()
print("\n")  # For Organization


def dem_states2012():
    """

    """
    print("---Top 5 Democrat States with the Highest Supporting Rate in 2012--- \n")  # Title for Output

    with open("1976-2016-president.csv") as myfile:  # Open the CSV File
        dem_states_2012 = []  # Variable to store output
        year = "2012"  # Criteria for year
        myfile_reader = csv.reader(myfile)
        for row in myfile_reader:
            if row[0] == year and row[8] == "democrat" and float(row[14][:len(row[14]) - 1]) > 61:  # Values to Search for
                print(row[1], "with a supporting rate of", row[14])  # Desired Output Layout
                dem_states_2012.append(row[14])  # Appending each output to the list

        return dem_states_2012

print("\n")  # For Organization


def rep_states2016():
    """

    """
    print("---Top 5 Republican States with the Highest Supporting Rate in 2016--- \n")  # Title for Output

    with open("1976-2016-president.csv") as myfile:  # Open the CSV File
        rep_states_2016 = []  # Variable to store output
        year = "2016"  # Criteria for year
        myfile_reader = csv.reader(myfile)
        for row in myfile_reader:
            if row[0] == year and row[8] == "republican" and float(row[14][:len(row[14]) - 1]) > 62.50:  # Values to Search for
                print(row[1], "with a supporting rate of", row[14])  # Desired Output Layout
                rep_states_2016.append(row[14])  # Appending each output to the list

        return rep_states_2016


print("\n")  # For Organization


def dem_states2016():
    print("---Top 5 Democrat States with the Highest Supporting Rate in 2016--- \n")  # Title for Output

    with open("1976-2016-president.csv") as myfile:  # Open the CSV File
        dem_states_2016 = []  # Variable to store output
        year = "2016"  # Criteria for year
        myfile_reader = csv.reader(myfile)
        for row in myfile_reader:
            if row[0] == year and row[8] == "democrat" and float(row[14][:len(row[14]) - 1]) > 59.00:  # Values to Search for
                print(row[1], "with a supporting rate of", row[14])  # Desired Output Layout
                dem_states_2016.append(row[14])  # Appending each output to the list

        return dem_states_2016


print("\n")  # For Organization
