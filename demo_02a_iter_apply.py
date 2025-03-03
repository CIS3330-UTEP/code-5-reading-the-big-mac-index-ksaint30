import pandas as pd

file_name = "./big-mac-full-index.csv"
df = pd.read_csv(file_name)

smol_df = df.query("index < 10")

def get_new_country_name(row):
    new_country_name = f"{row['name']} ({row["iso_a3"]})"
    return new_country_name

smol_df['name'] = smol_df.apply(get_new_country_name,axis=1)

print(smol_df)