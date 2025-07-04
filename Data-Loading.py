# Data Loading 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define countries of interest
countries_of_interest = ['Kenya', 'USA', 'India']

# Load the filtered dataset
filtered_df = pd.read_csv('cleaned_owid.csv')

# Ensure date is datetime
filtered_df['date'] = pd.to_datetime(filtered_df['date'])

# Handle missing data
filtered_df = filtered_df.dropna(subset=['total_vaccinations', 'population'])
filtered_df = filtered_df[filtered_df['total_vaccinations'] > 0]

# Calculate percent vaccinated
filtered_df['percent_vaccinated'] = (filtered_df['total_vaccinations'] / filtered_df['population']) * 100

# Line plot: Cumulative vaccinations
plt.figure(figsize=(12, 7))
colors = ['blue', 'green', 'red']
for i, country in enumerate(countries_of_interest):
    country_data = filtered_df[filtered_df['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country, color=colors[i], linewidth=2)
plt.title('Cumulative Vaccinations Over Time', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Total Vaccinations', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar plot: Percent vaccinated (latest date per country)
latest_vax = filtered_df.sort_values('date').groupby('location').tail(1)
plt.figure(figsize=(12, 7))
sns.barplot(data=latest_vax, x='location', y='percent_vaccinated', order=countries_of_interest, palette='Blues_d')
plt.title('Percentage of Vaccinated Population (Latest Date)', fontsize=14)
plt.xlabel('Country', fontsize=12)
plt.ylabel('% Vaccinated', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Debug data
print("\nData preview:")
print(filtered_df[['location', 'date', 'total_vaccinations', 'population', 'percent_vaccinated']].head())
print("\nMissing values:")
print(filtered_df[['total_vaccinations', 'population', 'percent_vaccinated']].isna().sum())