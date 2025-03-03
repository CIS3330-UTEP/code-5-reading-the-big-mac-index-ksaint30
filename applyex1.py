import pandas as pd
df = pd.read_csv("big-mac-full-index.csv")

smol_df = df.query("index < 10")

def get_year_from_date(row):
    # new_country_name =f"{row['date']}({row['iso_a3']})"
    # return row["date"][:4]
    return row["date"].split("-")[0]

new_col = df.apply(get_year_from_date,axis=1)
print(new_col)

df["year"] = new_col