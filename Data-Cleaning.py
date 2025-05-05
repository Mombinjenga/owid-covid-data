# --- Data Cleaning ---
# Import necessary libraries
import pandas as pd

# Load the dataset
df = pd.read_csv('owid.csv')

#Filter countries of interest 
countries_of_interest = ['Kenya', 'USA', 'India']
filtered_df = df[df['location'].isin(countries_of_interest)]

#Drop rows with missing dates or critical values
filtered_df = filtered_df.dropna(subset=['date', 'total_cases', 'total_deaths'])

#Convert the date column to datetime format
filtered_df['date'] = pd.to_datetime(filtered_df['date'])

#Handle missing numeric values 
numeric_columns = ['new_cases', 'new_deaths', 'total_vaccinations']
filtered_df[numeric_columns] = filtered_df[numeric_columns].interpolate()

# Display the cleaned dataset
print("\nCleaned dataset preview:")
print(filtered_df.head())

# Save the cleaned dataset to a new CSV file 
filtered_df.to_csv('owid.csv', index=False)