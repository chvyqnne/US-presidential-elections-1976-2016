import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("1976-2016-president.csv")


def total_votes():
    """
    Finds total number of U.S. votes for every election year from 2000 to 2016
    :return final_dictionary: total votes (value) for every election year (key)
    """

    past_2000 = df[df["year"] >= 2000]
    final_dictionary = {}

    # putting total candidate votes from every year into a dictionary
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
    Plots total number of votes in the U.S. from 2000-2016 in a line graph using data from total_votes()
    """

    data = total_votes()
    plt.plot(data.keys(), data.values(), color="g")
    plt.title("Total Votes in the U.S. From 2000-2016")
    plt.xlabel("Year")
    plt.ylabel("Votes")
    plt.savefig("totalvotes.png")
    return plt.show()


total_votes_map()
