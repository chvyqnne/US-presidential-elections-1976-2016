# Final Project Visualizations for Problems 3 & 4
# Cheyanne Cabang & Ricardo Sauerbrey

import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt
import os
from datetime import datetime

df = pd.read_csv("1976-2016-president.csv", index_col=0)  # Opening the data from the CSV file


# df['Date'] = df['Date'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d'))  # converting the Date format
# # year-month-date to years

# fig, ax = plt.subplots()
# df = df.sort_values("supportiverate", ascending=False)
# ax.bar(df.index, df["supportiverate"])
# ax.set_yticklabels(df.index, rotation=60, horizontalalignment="right", fontsize="4")
# ax.set_title("Support for Republican Party")
# plt.show()

# dataframe1 = df.sort_values("supportiverate", ascending=False)
# fig = plt.figure(figsize=(8, 5))
# ax1 = fig.add_subplot(1, 2, 1)
# ax1.bar(dataframe1.index, dataframe1["supportiverate"])
# ax1.set_yticklabels(dataframe1.index, rotation=60, horizontalalignment="right", fontsize="12")
# plt.show()

