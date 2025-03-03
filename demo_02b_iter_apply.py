import pandas as pd
df = pd.read_csv("./Session_10/big-mac-full-index.csv")

def get_year(row):
    return row["date"][0:4]

df["year"] = df.apply(get_year,axis=1)

print(df)