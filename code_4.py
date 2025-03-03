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
    smol_df = df[df["iso_a3"].str.lower() == country_code]  # Filter by country code
    price = smol_df["dollar_price"].mean()  # Get mean price
    return round(price, 2)


def get_the_cheapest_big_mac_price_by_year(year):
    smol_df = df.copy()  # Copy the DataFrame
    smol_df["year"] = smol_df["date"].str[:4]  # Extract the first 4 characters (year)
    
    smol_df = smol_df[smol_df["year"] == str(year)]  # Keep only rows from the given year

    cheapest_row = smol_df.nsmallest(1, "dollar_price").iloc[0]  # Get the row with the lowest price
    return round(price, 2)


def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    print(get_big_mac_price_by_year(2010, "can"))
    print(get_big_mac_price_by_country("can"))
    print(get_the_cheapest_big_mac_price_by_year("2014"))