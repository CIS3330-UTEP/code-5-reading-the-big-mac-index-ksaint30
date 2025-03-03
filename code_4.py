import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year, country_code):
    smol_df = df[df["iso_a3"].str.lower() == country_code]
    smol_df["year"] = smol_df["date"].str[:4]
    smol_df = smol_df[smol_df["year"] == str(year)]
    price = smol_df["dollar_price"].mean()  
    return round(price, 2)


def get_big_mac_price_by_country(country_code):
    smol_df = df[df["iso_a3"].str.lower() == country_code]
    price = smol_df["dollar_price"].mean()
    return round(price, 2)


def get_the_cheapest_big_mac_price_by_year(year):
    smol_df = df[df["date"].str[:4] == str(year)]  # No need for .copy()
    cheapest_row = smol_df.nsmallest(1, "dollar_price").iloc[0]
    return round(cheapest_row["dollar_price"], 2)


def get_the_most_expensive_big_mac_price_by_year(year):
    smol_df = df[df["date"].str[:4] == str(year)]
    most_expensive_row = smol_df.nlargest(1, "dollar_price").iloc[0]
    return round(most_expensive_row["dollar_price"], 2)


if __name__ == "__main__":
    print(get_big_mac_price_by_year(2010, "can"))
    print(get_big_mac_price_by_country("can"))
    print(get_the_cheapest_big_mac_price_by_year("2014"))
    print(get_the_most_expensive_big_mac_price_by_year("2014"))