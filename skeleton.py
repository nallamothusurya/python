#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import sys

# Function to convert wage string to numeric value
def convert_wage_to_numeric(wage_str):
    """
    Convert the player wage string to a numeric value.
    Handles 'K' for thousands and 'M' for millions, 
    and removes the euro symbol.
    """
    # Remove the euro symbol and any extra spaces
    wage_str = wage_str.replace('€', '').strip()
    
    # Convert based on suffix
    if wage_str[-1] == 'K':
        return float(wage_str[:-1]) * 1000  # 'K' means thousands
    elif wage_str[-1] == 'M':
        return float(wage_str[:-1]) * 1000000  # 'M' means millions
    else:
        try:
            return float(wage_str)  # Directly return if it's a simple number
        except ValueError:
            return 0  # Return 0 if the wage format is unexpected

# Function to calculate the mean overall score of players from a specified country
def mean_overall_country(df, country):
    """
    Calculate the mean overall score of players from a specified country.
    """
    # Filter players from the specified country
    country_players = df[df['Nationality'] == country]
    
    # Calculate and return the mean of the 'Overall' column
    return country_players['Overall'].mean()

# Function to calculate the mean wage (converted to numeric) of players from a specified club
def mean_wage_club(df, club):
    """
    Calculate the mean wage of players from a specified club.
    """
    # Filter players from the specified club
    club_players = df[df['Club'] == club].copy()
    
    # Apply the wage conversion function to the 'Wage' column
    club_players['Numeric Wage'] = club_players['Wage'].apply(convert_wage_to_numeric)
    
    # Return the mean of the numeric wage column
    return club_players['Numeric Wage'].mean()

# Function to find common players between a specified club and country
def common_players(df, club, country):
    """
    Find players who are part of both the specified club and country.
    """
    # Filter players by club and country
    club_players = df[df['Club'] == club]
    country_players = df[df['Nationality'] == country]
    
    # Find common players by merging the two dataframes on the 'Name' column
    common_players_df = pd.merge(club_players, country_players, how='inner', on='Name')
    
    # Return the list of common players' names
    return common_players_df['Name'].tolist()

# Main function to load data, perform tests, and return formatted results
def main(df, country_name, club_name):
    """
    Main function to process the data, calculate the required values, and print results.
    """
    # Finding common players between the club and the country
    common_players_list = common_players(df, club_name, country_name)

    # Calculating the mean overall score of players from the country
    mean_country_overall = mean_overall_country(df, country_name)

    # Calculating the mean wage of players from the club
    mean_club_wage = mean_wage_club(df, club_name)

    # Round the values to two decimal places and ensure they are Python float types
    mean_country_overall = round(mean_country_overall, 2)
    mean_club_wage = round(mean_club_wage, 2)

    # Print the results: common players, mean overall score, and mean wage
    # Convert to a native Python float to avoid np.float64 type
    print([", ".join(common_players_list), float(mean_country_overall), float(mean_club_wage)])

if __name__ == "__main__":
    # Read the dataset (first 100 rows)
    df = pd.read_csv('data.csv').head(100)
    
    # Ensure the script is executed with the required arguments (country and club)
    if len(sys.argv) < 3:
        print("Please provide both a country and a club name as arguments.")
        sys.exit(1)
    
    # Execute the main function with country and club passed as command-line arguments
    main(df, sys.argv[1], sys.argv[2])
