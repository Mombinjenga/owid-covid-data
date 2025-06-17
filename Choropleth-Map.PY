# Choropleth map

import pandas as pd
import plotly.express as px
import plotly.io as pio
import numpy as np

# Set Plotly renderer for Jupyter
pio.renderers.default = 'notebook'

# Load the original dataset
df = pd.read_csv('owid-covid-data-old.csv')

# Ensure date is datetime
df['date'] = pd.to_datetime(df['date'])

# Prepare data for the latest date
latest_data = df[df['date'] == df['date'].max()].copy()

# Handle missing data
latest_data = latest_data.dropna(subset=['iso_code', 'total_cases', 'total_vaccinations', 'population'])
latest_data = latest_data[latest_data['total_cases'] > 0]

# Calculate vaccination rate and log cases
latest_data['vaccination_rate'] = (latest_data['total_vaccinations'] / latest_data['population']) * 100
latest_data['vaccination_rate'] = latest_data['vaccination_rate'].clip(upper=100)
latest_data['log_total_cases'] = np.log1p(latest_data['total_cases'])

# Choropleth for total cases
fig = px.choropleth(
    latest_data,
    locations="iso_code",
    color="log_total_cases",
    hover_name="location",
    title="Total COVID-19 Cases by Country (Log Scale)",
    color_continuous_scale="Reds",
    projection="natural earth",
)
fig.update_layout(
    coloraxis_colorbar=dict(title="Log(Total Cases)"),
    title={'text': "Total COVID-19 Cases by Country", 'x': 0.5, 'xanchor': 'center'},
    geo=dict(showframe=False, showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="LightGrey")
)
fig.show()

# Choropleth for vaccination rates
fig = px.choropleth(
    latest_data,
    locations="iso_code",
    color="vaccination_rate",
    hover_name="location",
    title="Vaccination Rates by Country",
    color_continuous_scale="Blues",
    projection="natural earth"
)
fig.update_layout(
    coloraxis_colorbar=dict(title="% Vaccinated"),
    title={'text': "Vaccination Rates by Country", 'x': 0.5, 'xanchor': 'center'},
    geo=dict(showframe=False, showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="LightGrey")
)
# Optional: Zoom to Kenya, USA, India
# fig.update_geos(fitbounds="locations", visible=True)
fig.show()

# Debug data
print("\nLatest data preview:")
print(latest_data[['location', 'iso_code', 'total_cases', 'vaccination_rate']].head())
print("\nMissing values:")
print(latest_data[['iso_code', 'total_cases', 'total_vaccinations', 'population']].isna().sum())