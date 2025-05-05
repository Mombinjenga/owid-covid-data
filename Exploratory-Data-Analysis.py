import pandas as pd

# Load the cleaned dataset
filtered_df = pd.read_csv('owid.csv')

# Ensure the 'date' column is in datetime format
filtered_df['date'] = pd.to_datetime(filtered_df['date'])

import matplotlib.pyplot as plt
import seaborn as sns

# Ensure 'countries_of_interest' and 'filtered_df' are defined
countries_of_interest = ['Kenya', 'USA', 'India']  # Example countries
# Ensure 'filtered_df' is created from your cleaned dataset

# Plot total cases over time for selected countries
plt.figure(figsize=(10, 6))
for country in countries_of_interest:
    country_data = filtered_df[filtered_df['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)
plt.title('Total Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot total deaths over time for selected countries
plt.figure(figsize=(10, 6))
for country in countries_of_interest:
    country_data = filtered_df[filtered_df['location'] == country]
    plt.plot(country_data['date'], country_data['total_deaths'], label=country)
plt.title('Total Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Compare daily new cases between countries
plt.figure(figsize=(10, 6))
sns.barplot(data=filtered_df, x='location', y='new_cases', ci=None, order=countries_of_interest)
plt.title('Daily New Cases Comparison')
plt.xlabel('Country')
plt.ylabel('New Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Calculate the death rate and plot
filtered_df['death_rate'] = filtered_df['total_deaths'] / filtered_df['total_cases']
plt.figure(figsize=(10, 6))
for country in countries_of_interest:
    country_data = filtered_df[filtered_df['location'] == country]
    plt.plot(country_data['date'], country_data['death_rate'], label=country)