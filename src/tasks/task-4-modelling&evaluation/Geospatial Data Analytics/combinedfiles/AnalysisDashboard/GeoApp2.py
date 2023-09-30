import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Set the page layout to "wide"
st.set_page_config(layout="wide")

# Load the dataset
def load_data():
    data = pd.read_csv("GeoData.csv")
    return data

data = load_data()

# Center-align the page title
st.markdown(
    f'<h1 style="text-align: center;">Germany<br>Waste-Management Stations<br> GeoSpatial Analysis</h1>',
    unsafe_allow_html=True
)

# Create a new DataFrame to store station counts by state and type
station_counts = data.groupby(['state', 'station']).size().unstack(fill_value=0)

# Calculate the total stations for each state
station_counts['Total Stations'] = station_counts.sum(axis=1)

# Calculate the totals for each station type
station_type_totals = station_counts.sum(axis=0)
station_type_totals.name = 'Total'

# Concatenate the totals row to the bottom of the DataFrame
station_counts = pd.concat([station_counts, station_type_totals.to_frame().T])

# Define the layout for the table
st.markdown(
    f'<h2 style="color: lightgreen"><br><br>Station Information Table</h2>',
    unsafe_allow_html=True
)

# Create a multiselect dropdown for states
selected_states = st.multiselect("Select States", data['state'].unique(), default=data['state'].unique())

# Filter the data based on selected states
filtered_data = data[data['state'].isin(selected_states)]

# Display the table with state-wise station counts
st.table(station_counts[station_counts.index.isin(selected_states)].reset_index())

# Calculate the totals for each station type
station_type_totals = station_counts.sum(axis=0)
station_type_totals.name = 'Total'

# Concatenate the totals row to the bottom of the DataFrame
station_counts = pd.concat([station_counts, station_type_totals.to_frame().T])

# Define the layout for the grid
st.header("Station Information Grid")

# Create a list to store station types and their corresponding colors
station_info = [
    {
        'name': 'Landfills',
        'type': 'landfills',
        'color': 'lightgreen'
    },
    {
        'name': 'Waste Disposal Centres',
        'type': 'waste disposal centres',
        'color': 'lightblue'
    },
    {
        'name': 'Recycling Centres',
        'type': 'recycling centres',
        'color': 'lightyellow'
    },
    {
        'name': 'Waste Transfer Stations',
        'type': 'waste transfer stations',
        'color': 'lightpink'
    }
]

# Create a 2x2 grid for station types
col1, col2 = st.columns(2)

for info in station_info:
    station_name = info['name']
    station_type = info['type']
    filtered_data_by_type = filtered_data[filtered_data['station'] == station_type]
    station_count = len(filtered_data_by_type)

    # Display station information in a grid cell with styles and spacing
    with col1 if info['name'] in ('Landfills', 'Waste Disposal Centres') else col2:
        st.markdown(
            f'<div class="grid-item" style="background-color: {info["color"]}; padding: 20px; '
            f'border-radius: 5px; color: black; margin-bottom: 20px;">'
            f'<h3 style="color: black;">{station_name}</h3>'
            f'<p style="color: brown;">Total Stations: {station_count}</p>'
            f'</div>',
            unsafe_allow_html=True
        )

# Create a DataFrame to store station counts by state and type
station_counts_by_type = filtered_data.groupby(['state', 'station']).size().unstack(fill_value=0)

# Calculate the total stations for each state
station_counts_by_type['Total Stations'] = station_counts_by_type.sum(axis=1)

# Create a heat map on the right using Plotly
st.header("Heat Map of Stations by State")
fig = px.choropleth(station_counts_by_type, 
                    geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/germany.geojson', 
                    locations=station_counts_by_type.index,  # Use the state names from the index
                    color='Total Stations',
                    hover_name=station_counts_by_type.index,  # Use the state names from the index
                    hover_data={'Total Stations': True},
                    locationmode="geojson-id",  # Corrected locationmode
                    labels={'Total Stations':'Total Stations'},
                    title='Station Heat Map')
fig.update_geos(fitbounds="locations", visible=False)
st.plotly_chart(fig, use_container_width=True)

# Create a DataFrame to store station counts by state and type
station_counts_by_type = filtered_data.groupby(['state', 'station']).size().unstack(fill_value=0)

# Calculate the total stations for each state
station_counts_by_type['Total Stations'] = station_counts_by_type.sum(axis=1)

# Create a heatmap of states based on the Station Information Table
st.header("Heatmap of States Based on Station Information")

# fig = px.imshow(station_counts_by_type.iloc[:, :-1], 
#                 color_continuous_scale='Viridis', 
#                 labels=dict(index="State"))

# # Adjust the aspect ratio to focus more on the x-axis
# fig.update_layout(
#     aspectratio=dict(x=3, y=1),  # Increase the x-axis aspect ratio
#     xaxis_fixedrange=True  # Lock the x-axis range
# )

# # Display the heatmap
# st.plotly_chart(fig, use_container_width=True)

# Create a heatmap using Plotly's go.Figure
heatmap_data = station_counts.iloc[:, :-1]  # Exclude the "Total Stations" column
fig = go.Figure(data=go.Heatmap(
    z=heatmap_data.values,  # Values for the heatmap
    x=heatmap_data.columns,  # X-axis labels
    y=heatmap_data.index,  # Y-axis labels
    colorscale='Viridis',  # Color scale
    colorbar=dict(title='Station Count'),  # Color bar title
))

# Adjust the aspect ratio to stretch the x-axis
fig.update_layout(
    autosize=False,
    width=500,  # Adjust the width as needed
    height=500,  # Adjust the height as needed
)

# Display the heatmap
st.plotly_chart(fig, use_container_width=True)
