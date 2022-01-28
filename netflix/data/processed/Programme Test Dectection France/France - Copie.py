from collections import Counter
import pandas as pd
import csv

with open('merged.csv', 'r', encoding='utf-8', newline='') as csv_file:

    df = pd.read_csv("merged.csv",
                     index_col=["type","country"])
                     #usecols=["NOC","Medal"])
    #df.sort_index()

    #grouped = df.groupby(['NOC', 'Medal'])

    grouped = df.groupby(['type','country'])['type'].count()

print(grouped)