# Data Cleaning

import pandas as pd

# Load the original dataset
df = pd.read_csv('owid-covid-data-old.csv')

# Filter for countries of interest
countries_of_interest = ['Kenya', 'USA', 'India']
filtered_df = df[df['location'].isin(countries_of_interest)]

# Drop rows with missing critical values
filtered_df = filtered_df.dropna(subset=['date', 'total_cases', 'total_deaths', 'population', 'iso_code'])

# Convert date to datetime
filtered_df['date'] = pd.to_datetime(filtered_df['date'])

# Interpolate missing numeric values
numeric_columns = ['new_cases', 'new_deaths', 'total_vaccinations']
filtered_df[numeric_columns] = filtered_df[numeric_columns].interpolate()

# Display cleaned dataset preview
print("\nCleaned dataset preview:")
print(filtered_df[['location', 'date', 'total_cases', 'total_deaths', 'total_vaccinations', 'population', 'iso_code']].head())
print("\nMissing values:")
print(filtered_df[['total_cases', 'total_deaths', 'total_vaccinations', 'population', 'iso_code']].isna().sum())

# Save to a new CSV file
filtered_df.to_csv('cleaned_owid.csv', index=False)
print("\nCleaned data saved to 'cleaned_owid.csv'")