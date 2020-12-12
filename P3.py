# Final Project Question 3
# Cheyanne Cabang & Ricardo Sauerbrey

import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

file = pd.read_csv("1976-2016-president.csv")  # Import the file to Python


def rep_states2012():
    """
    Prints the top 5 Republican states with the highest supporting rates in the 2012 U.S. election
    """

    print("---Top 5 Republican States with the Highest Supporting Rate in 2012--- \n")  # Title for Output

    with open("1976-2016-president.csv") as myfile:  # Open the CSV File
        rep_states_2012 = []  # Variable to store output
        year = "2012"  # Criteria for year
        myfile_reader = csv.reader(myfile)  # Read the CSV file

        for row in myfile_reader:
            if row[0] == year and row[8] == "republican" and float(row[14][:len(row[14]) - 1]) > 62.29:  # Values to Search for
                print(row[1], "with a supporting rate of", row[14])  # Desired Output Layout
                rep_states_2012.append((row[1], float(row[14].strip("%"))))  # Appending each output to the list

        return rep_states_2012


print("\n")  # For Organization


def dem_states2012():
    """
    Prints the top 5 Democrat states with the highest supporting rates in the 2012 U.S. election
    """

    print("---Top 5 Democrat States with the Highest Supporting Rate in 2012--- \n")  # Title for Output

    with open("1976-2016-president.csv") as myfile:  # Open the CSV File
        dem_states_2012 = []  # Variable to store output
        year = "2012"  # Criteria for year
        myfile_reader = csv.reader(myfile)

        for row in myfile_reader:
            if row[0] == year and row[8] == "democrat" and float(row[14][:len(row[14]) - 1]) > 61:  # Values to Search for
                print(row[1], "with a supporting rate of", row[14])  # Desired Output Layout
                dem_states_2012.append((row[1], float(row[14].strip("%"))))  # Appending each output to the list

        return dem_states_2012


print("\n")  # For Organization


def rep_states2016():
    """
    Prints the top 5 Republican states with the highest supporting rates in the 2016 U.S. election
    """

    print("---Top 5 Republican States with the Highest Supporting Rate in 2016--- \n")  # Title for Output

    with open("1976-2016-president.csv") as myfile:  # Open the CSV File
        rep_states_2016 = []  # Variable to store output
        year = "2016"  # Criteria for year
        myfile_reader = csv.reader(myfile)
        for row in myfile_reader:
            if row[0] == year and row[8] == "republican" and float(row[14][:len(row[14]) - 1]) > 62.50:  # Values to Search for
                print(row[1], "with a supporting rate of", row[14])  # Desired Output Layout
                rep_states_2016.append((row[1], float(row[14].strip("%"))))  # Appending each output to the list

        return rep_states_2016


print("\n")  # For Organization


def dem_states2016():
    """
    Prints the top 5 Democrat states with the highest supporting rates in the 2016 U.S. election
    """

    print("---Top 5 Democrat States with the Highest Supporting Rate in 2016--- \n")  # Title for Output

    with open("1976-2016-president.csv") as myfile:  # Open the CSV File
        dem_states_2016 = []  # Variable to store output
        year = "2016"  # Criteria for year
        myfile_reader = csv.reader(myfile)

        for row in myfile_reader:
            if row[0] == year and row[8] == "democrat" and float(row[14][:len(row[14]) - 1]) > 59.00:  # Values to Search for
                print(row[1], "with a supporting rate of", row[14])  # Desired Output Layout
                dem_states_2016.append((row[1], float(row[14].strip("%"))))  # Appending each output to the list

        return dem_states_2016


print("\n")  # For Organization


def dem_states_2012_plot():
    """
    Plots top 5 democrat states in 2012
    """

    data = dem_states2012()
    state = []
    supporting_rates = []

    for i in data:
        state.append(i[0])
        supporting_rates.append(i[1])

    dataframe = pd.DataFrame({"State": state, "Supporting Rates": supporting_rates}, index=state)
    dataframe = dataframe.sort_values("Supporting Rates")
    dataframe.plot(kind="barh", color="blue")
    plt.gcf().subplots_adjust(bottom=0.15, left=0.3)
    plt.title("Top 5 Democrat-supporting States in 2012")
    plt.xlabel("Supporting Rates (%)")
    plt.ylabel("State")
    plt.savefig("demstates2012.png")
    return plt.show()


def rep_states_2012_plot():
    """
    Plots top 5 republican states in 2012
    """

    data = rep_states2012()
    state = []
    supporting_rates = []

    for i in data:
        state.append(i[0])
        supporting_rates.append(i[1])

    dataframe = pd.DataFrame({"State": state, "Supporting Rates": supporting_rates}, index=state)
    dataframe = dataframe.sort_values("Supporting Rates")
    dataframe.plot(kind="barh", color="r")
    plt.gcf().subplots_adjust(bottom=0.15, left=0.3)
    plt.title("Top 5 Republican-supporting States in 2012")
    plt.xlabel("Supporting Rates (%)")
    plt.ylabel("State")
    plt.savefig("repstates2012.png")
    return plt.show()


def dem_states_2016_plot():
    """
    Plots top 5 democrat states in 2016
    """

    data = dem_states2016()
    state = []
    supporting_rates = []

    for i in data:
        state.append(i[0])
        supporting_rates.append(i[1])

    dataframe = pd.DataFrame({"State": state, "Supporting Rates": supporting_rates}, index=state)
    dataframe = dataframe.sort_values("Supporting Rates")
    dataframe.plot(kind="barh", color="blue")
    plt.gcf().subplots_adjust(bottom=0.15, left=0.3)
    plt.title("Top 5 Democrat-supporting States in 2016")
    plt.xlabel("Supporting Rates (%)")
    plt.ylabel("State")
    plt.savefig("demstates2016.png")
    return plt.show()


def rep_states_2016_plot():
    """
    Plots top 5 republican states in 2016
    """

    data = rep_states2016()
    state = []
    supporting_rates = []

    for i in data:
        state.append(i[0])
        supporting_rates.append(i[1])

    dataframe = pd.DataFrame({"State": state, "Supporting Rates": supporting_rates}, index=state)
    dataframe = dataframe.sort_values("Supporting Rates")
    dataframe.plot(kind="barh", color="r")
    plt.gcf().subplots_adjust(bottom=0.15, left=0.3)
    plt.title("Top 5 Republican-supporting States in 2016")
    plt.xlabel("Supporting Rates (%)")
    plt.ylabel("State")
    plt.savefig("repstates2016.png")
    return plt.show()

