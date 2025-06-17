import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('owid.csv')

# Ensure the 'date' column is in datetime format
df['date'] = pd.to_datetime(df['date'])

# Prepare a dataframe with iso_code, total_cases, and vaccination rates for the latest date
latest_data = df[df['date'] == df['date'].max()].copy()

# Plot a choropleth map for total cases
fig = px.choropleth(
    latest_data,
    locations="iso_code",  # Column with ISO country codes
    color="total_cases",  # Column to visualize
    hover_name="location",  # Column to display on hover
    title="Total COVID-19 Cases by Country",
    color_continuous_scale="Reds",
    projection="natural earth"
)
fig.show()

#Plot a choropleth map for vaccination rates
latest_data['vaccination_rate'] = (latest_data['total_vaccinations'] / latest_data['population']) * 100
fig = px.choropleth(
    latest_data,
    locations="iso_code",
    color="vaccination_rate",
    hover_name="location",
    title="Vaccination Rates by Country",
    color_continuous_scale="Blues",
    projection="natural earth"
)
fig.show()