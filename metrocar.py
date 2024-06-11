# -*- coding: utf-8 -*-
"""metroCar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TU0zKzOkIcjn-1cfae1Zd6GvMOtAdpuJ
"""

import glob
import pandas as pd

# Define the pattern for the CSV files (e.g., all CSV files in a directory)
file_pattern = '*.csv'

# Use glob to find all files matching the pattern
csv_files = glob.glob(file_pattern)


df = pd.DataFrame()

# Loop through the files and read them into dataframes
for file in csv_files:
    data = pd.read_csv(file)
    df = pd.concat([df, data], ignore_index=True)

df.head()

df.shape

df.columns

df2 = df.groupby('user_id', as_index=False)['purchase_amount_usd'].sum()
df2.head()

df3 = df.drop_duplicates('user_id')

df3.shape

df3 = df3[~df3['user_id'].isna()]  # remove the single null row in user_id column

df3.drop('purchase_amount_usd', axis = 1, inplace =True)

df3.shape  # data in shape

frame = df2.merge(df3, on = 'user_id', how='inner')  # merging both dataframes

frame.head()

frame.shape

frame.to_csv('metro_car.csv', index=False)  # saved for tableau processing.