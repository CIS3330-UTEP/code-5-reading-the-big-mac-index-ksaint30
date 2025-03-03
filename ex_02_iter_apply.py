# Write a function that receives one parameter (row) and then 
# returns the year from the date column in that row
# Use the apply method to apply your function over the big mac 
# index dataframe and save the results to a new column ["year"] 
# in your dataframe

import pandas as pd

big_mac_file = './big-mac-full-index.csv'
file_name = "./big-mac-full-index.csv"
df = pd.read_csv(file_name)

def get_year_from_date(row):
    # return row["date"][:4]
    return row["date"].split("-")[0]

new_col = df.apply(get_year_from_date,axis=1)
# print(new_col)

df["year"] = new_col

print(df)