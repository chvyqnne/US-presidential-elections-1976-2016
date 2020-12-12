import pandas
import csv
import matplotlib.pyplot as plt
import itertools

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
                print(row[1], "in", row[0], "had", row[10], "votes for the Republican party.")  # Desired Output Layout
                fl_rep_votes.append([repvotes])  # Appending each output to the list
                new_fl_rep_votes = list(itertools.chain.from_iterable(fl_rep_votes))  # Converts a nested list into a
                # single list
                new2_fl_rep_votes = [int(i) for i in new_fl_rep_votes]  # Converts votes from strings to integers

        return new2_fl_rep_votes


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
                new_fl_dem_votes = [int(i) for i in fl_dem_votes]  # Converts votes from strings to integers

        return new_fl_dem_votes


def florida_rep_votes_plot():
    """
    Plots Florida Republican votes from 1976-2016
    """

    data = fl_repvotes()
    year = [1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016]
    plt.plot(year, data, color='red')
    plt.title("Florida Votes Over Time 1976-2016 for the Republican Party")
    plt.xlabel("Year")
    plt.ylabel("Votes (millions)")
    plt.savefig("flrepvotes.png")
    return plt.show()


florida_rep_votes_plot()


def florida_dem_votes_plot():
    """
    Plots Florida Democrat votes from 1976-2016
    """

    data = fl_demvotes()
    year = [1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016]
    plt.plot(year, data, color='blue')
    plt.title("Florida Votes Over Time 1976-2016 for the Democratic Party")
    plt.xlabel("Year")
    plt.ylabel("Votes (millions)")
    plt.savefig("fldemvotes.png")
    return plt.show()


florida_dem_votes_plot()
