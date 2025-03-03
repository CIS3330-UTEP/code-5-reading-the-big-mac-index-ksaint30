import pandas as pd
df = pd.read_csv("big-mac-full-index.csv")
# Can use df.loc[index] instead of df.iloc[index] to prevent falling out of bounds
smol_df = df.query("index < 10")
for index, row in df.iterrows():
    # print(row["name"])
    # if df['dollar_price'][index] < 1:
    #     print(df['dollar_price'][index])
    if row["dollar_price"] < 1:
        print(row["dollar_price"])