import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("1976-2016-president.csv")

def total_non_rd():
    """
    Finds total number of non-Republican and non-Democrat votes in the U.S. from 1976-2016
    :return data: dictionary of total votes for non-R & D candidates for every election year
    """

    non_rd = df[(df["party"] != "republican") | (df["party"] != "democrat")]
    data = {}

    # putting non-RD candidate votes from every year into a dictionary
    for index, row in non_rd.iterrows():
        year = str(row["year"])
        votes = row["candidatevotes"]

        if year in data:
            data[year] += votes
        else:
            data[year] = votes

    return data


def total_non_rd_map():
    """
    Plots data from total_non_rd() into a line graph
    """

    data = total_non_rd()
    plt.plot(data.keys(), data.values(), color="orange")
    plt.title("Non-Republican and Non-Democrat Votes in U.S. From 1976-2016")
    plt.xlabel("Year")
    plt.ylabel("Votes")
    return plt.show()

total_non_rd_map()
