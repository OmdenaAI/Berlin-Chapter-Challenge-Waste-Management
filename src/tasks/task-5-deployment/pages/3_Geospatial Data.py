import streamlit as st
import webbrowser
import pandas as pd
import numpy as np
import json 
import pickle 
import requests 
import folium
import pyproj
import warnings
from haversine import haversine, Unit 

warnings.filterwarnings('ignore')


st.title("Geospatial Data Analytics")
st.write(
                    "Clear and concise route information is presented to users, ensuring they have a comprehensive understanding of selected paths. "
                    "Moreover, users can conveniently download visualizations in .png format, facilitating seamless sharing and integration into various reports and presentations."
                )

st.write("Enter latitude and longitude coordinates to display a map:")

user_latitude = st.number_input("Enter Latitude:")
user_longitude = st.number_input("Enter Longitude:")

# Replace with your API key
api_key = "5b3ce3597851110001cf62481812d7fb40e0470695b078ee763d603e"

config = {
    'directory_data': 'combinedfiles/',
    'input_file_name': 'station_cluster_centers.csv',
    'output_file_name': 'shortest_path.pkl',
    'clusters_path': 'station_cluster_centers.csv',
    'threshold_in_meters': 500,
    'station_categories': ['waste disposal centres', 'waste transfer stations', 'landfills', 'recycling centres'],
    'germany_map_center': [51.1657, 10.4515],
    'waste_transfer_clusters' :'waste_transfer_clusters.csv',
    'recycling_centre_clusters':'recycling_clusters',
    'station2color_map': {'waste disposal centres': 'lightblue', 'waste transfer stations': 'gray',
                          'landfills': 'lightred', 'recycling centres': 'lightgreen'},
    'cluster2color_map': {'waste disposal centres': 'darkblue', 'waste transfer stations': 'black',
                          'landfills': 'red', 'recycling centres': 'darkgreen'}
}

# Replace with your specific latitude and longitude coordinates for the starting and ending points
start_latitude = user_latitude
start_longitude = user_longitude
waste_transfer_lat = 0
waste_transfer_lon = 0
recycling_lat = 49.420318
recycling_lon = 8.687872


def find_closest_waste_disposal_cluster(user_input_latitude, user_input_longitude, clusters_file_path):
    """
    Finds the closest waste disposal cluster to the user's input coordinates.
    """
    # Load the cluster data from the CSV file
    clusters_df = pd.read_csv(clusters_file_path)

    # Initialize variables for minimum distance and selected cluster ID
    min_distance = float('inf')  # Initialize with positive infinity
    selected_cluster_id = None

    # Create a tuple for the user input coordinates
    user_input_coords = (user_input_latitude, user_input_longitude)

    # Iterate through each cluster in the DataFrame
    for index, row in clusters_df.iterrows():
        cluster_coords = (row['cluster_lat'], row['cluster_lon'])
        
        # Calculate the distance from the user input location to the cluster using Haversine
        distance_to_cluster = haversine(user_input_coords, cluster_coords, unit=Unit.KILOMETERS)
        
        # Check if this cluster is closer than the previous closest one
        if distance_to_cluster < min_distance:
            min_distance = distance_to_cluster
            selected_cluster_id = row['cluster_ID']

    return selected_cluster_id





if user_latitude and user_longitude:
    find_closest_waste_disposal_cluster(start_latitude,start_longitude,'waste_transfer_clusters.csv')
    if response.status_code == 200:
        
        # Define the URL with the parameters
        url = f'https://api.openrouteservice.org/v2/directions/driving-hgv?api_key={api_key}&start={start_longitude},{start_latitude}&end={end_longitude},{end_latitude}'

        # Define the headers for the request
        headers = {
            'Accept': 'application/json, application/geo+json',
        }

        # Make the GET request to ORS Directions API
        response = requests.get(url, headers=headers)
        geojson_data = response.json()  # Updated variable name
        
        # Save the GeoJSON data to a .geojson file
        with open('route_data.geojson', 'w') as geojson_file:
            json.dump(geojson_data, geojson_file)
        print("Route data saved as 'route_data.geojson'")
    else:
        print("Error: Unable to fetch route data")

    # Load the GeoJSON data from the file
    with open('route_data.geojson', 'r') as geojson_file:
        geojson_data = json.load(geojson_file)

    # Create a Folium map centered on the route
    m = folium.Map(location=[49.41461, 8.681495], zoom_start=15)

    # Add the GeoJSON data to the map as a GeoJson object
    folium.GeoJson(geojson_data).add_to(m)

    # Display the map
    m.save('route_map.html')
else:
    st.warning("Please enter latitude and longitude coordinates.")