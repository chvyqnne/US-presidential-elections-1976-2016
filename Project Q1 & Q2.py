import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("1976-2016-president.csv")


def total_votes():
    """
    Finds total number of U.S. votes for every election year from 2000 to 2016
    :return final_dictionary: total votes (value) for every election year (key)
    """

    past_2000 = df[df["year"] >= 2000]
    final_dictionary = {}

    for index, row in past_2000.iterrows():
        year = str(row["year"])
        votes = row["candidatevotes"]

        if year in final_dictionary:
            final_dictionary[year] += votes
        else:
            final_dictionary[year] = votes

    return final_dictionary


def total_votes_map():
    """
    Plots total number of votes in the U.S. from 2000-2016 in a line graph
    """

    data = total_votes()
    plt.plot(data.keys(), data.values(), color="g")
    plt.title("Total Votes in the U.S. From 2000-2016")
    plt.xlabel("Year")
    plt.ylabel("Votes")
    return plt.show()


def compare_votes(state):
    """
    Compares the number of votes and percentages for Republicans and Democrats for any state from 2000-2016
    :param state: any state in the U.S. from the df
    :return results: tuple of election year, party, total votes, and percentage of votes for that party, separated by party
    """

    past_2000 = df[df["year"] >= 2000]  # narrowing dataframe to election results after 2000
    state = past_2000[past_2000["state"] == state]  # narrowing to selected state
    # getting total votes (including independents) to calculate percentages
    votes = state.loc[((state["party"] == "democrat") | (state["party"] == "republican")), "totalvotes"]
    results = []

    for ind in state.index:
        # finding total votes and percentage for democratic candidate over the years
        if state["party"][ind] == "democrat":
            democrat_votes = state["candidatevotes"][ind]
            democrat_percent = democrat_votes / votes * 100
            results.append((state["year"][ind], state["party"][ind], democrat_votes, round(democrat_percent[ind], 2)))

        # finding total votes and percentage for republican candidate over the years
        elif state["party"][ind] == "republican":
            republican_votes = state["candidatevotes"][ind]
            republican_percent = republican_votes / votes * 100
            results.append((state["year"][ind], state["party"][ind], republican_votes, round(republican_percent[ind], 2)))

    return results


def compare_votes_map(state):
    """
    Compares Republican and Democrat votes from 2000-2016 in chosen state using line graph and results from compare_votes()
    :param state: chosen state from dataframe
    :return: stacked bar graph
    """

    s = compare_votes(state)
    # taking every election year
    year = [2000, 2004, 2008, 2012, 2016]
    republican_votes = []
    democrat_votes = []

    # total votes for each party for every election year
    for i in s:
        if "republican" in i:
            republican_votes.append(i[2])
        elif "democrat" in i:
            democrat_votes.append(i[2])

    plt.bar(year, democrat_votes, width=1.75, label="democrat votes", color="blue")
    plt.bar(year, republican_votes, bottom=np.array(democrat_votes), width=1.75, label="republican votes", color="red")
    plt.title("Total Republican and Democrat Votes From 2000 to 2016")
    plt.xlabel("Election Year")
    plt.ylabel("Total Votes")
    plt.legend(loc="upper left")
    plt.xticks([2000, 2004, 2008, 2012, 2016])
    return plt.show()


print(compare_votes(""))
compare_votes_map("")

# TODO: plot the results of an election year on a US map w/ diff colors representing R & D


# TODO: find 2 other insights that you think are valuable and interpret them
# total votes for non r & d over time

