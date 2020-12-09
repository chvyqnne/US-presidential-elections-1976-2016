import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("1976-2016-president.csv")


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