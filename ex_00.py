import pandas as pd
df = pd.read_csv("big-mac-full-index.csv")

print(type(df["date"][0]))

date =7 

query = "date >= '2018-01-1 and date < 2019-01-01'"
# query2 = "date < 2019-01-01"
df = df.query(query)
# df = df.query(query2)

print(df)