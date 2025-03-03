import pandas as pd
df = pd.read_csv("big-mac-full-index.csv")
# Can use df.loc[index] instead of df.iloc[index] to prevent falling out of bounds
smol_df = df.query("index < 10")
for index, row in df.iterrows():
    print(row["USD_adjusted"])
    # print(df['name'][index])