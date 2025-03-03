# Write code that will iterate over the big-mac-index and print 
# the dollar_price any time the dollar_price is less than 1 using 
# iterrows

import pandas as pd

file_name = "./big-mac-full-index.csv"
df = pd.read_csv(file_name)

for idx, row in df.iterrows():
    if row["dollar_price"] < 1:
        print(row["dollar_price"])