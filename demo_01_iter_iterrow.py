import pandas as pd

file_name = "./big-mac-full-index.csv"
df = pd.read_csv(file_name)

# smol_df = df.query("index < 10")

for index, row in df.iterrows():
    print(row["name"])
    # print(df.loc[index])
    print(df["name"][index])