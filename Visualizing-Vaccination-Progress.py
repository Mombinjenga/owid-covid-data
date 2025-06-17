# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define countries of interest
countries_of_interest = ['Kenya', 'USA', 'India']  # Example countries

# Load the dataset
df = pd.read_csv('owid.csv')

# Define filtered_df from the dataset
filtered_df = df[df['location'].isin(countries_of_interest)].copy()


# Ensure the 'date' column is in datetime format
filtered_df['date'] = pd.to_datetime(filtered_df['date'])

# Plot cumulative vaccinations over time for selected countries
plt.figure(figsize=(10, 6))
for country in countries_of_interest:
    country_data = filtered_df[filtered_df['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)
plt.title('Cumulative Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Compare % vaccinated population
plt.figure(figsize=(10, 6))
filtered_df['percent_vaccinated'] = (filtered_df['total_vaccinations'] / filtered_df['population']) * 100
sns.barplot(data=filtered_df, x='location', y='percent_vaccinated', ci=None, order=countries_of_interest)
plt.title('Percentage of Vaccinated Population')
plt.xlabel('Country')
plt.ylabel('% Vaccinated')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()