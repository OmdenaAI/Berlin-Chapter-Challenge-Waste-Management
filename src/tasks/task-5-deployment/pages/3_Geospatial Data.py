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
from streamlit_folium import folium_static


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
    'waste_transfer_clusters' :'combinedfiles/waste_transfer_clusters.csv',
    'recycling_centre_clusters':'recycling_clusters',
    'station2color_map': {'waste disposal centres': 'lightblue', 'waste transfer stations': 'gray',
                          'landfills': 'lightred', 'recycling centres': 'lightgreen'},
    'cluster2color_map': {'waste disposal centres': 'darkblue', 'waste transfer stations': 'black',
                          'landfills': 'red', 'recycling centres': 'darkgreen'}
}

# Replace with your specific latitude and longitude coordinates for the starting and ending points

start_latitude = float(user_latitude)
start_longitude = float(user_longitude)


def find_closest_cluster(user_input_latitude, user_input_longitude, clusters_file_path):
    """
    Finds the closest waste disposal cluster to the user's input coordinates.
    """
    # Load the cluster data from the CSV file
    clusters_df = pd.read_csv(clusters_file_path)

    # Initialize variables for minimum distance and selected cluster ID
    min_distance = float('inf')  # Initialize with positive infinity
    selected_cluster_coords = None  # Initialize as None

    # Create a tuple for the user input coordinates
    user_input_coords = (user_input_latitude, user_input_longitude)

    for index, row in clusters_df.iterrows():
        cluster_coords = (row['cluster_lat'], row['cluster_lon'])
        
        # Calculate the distance from the user input location to the cluster using Haversine
        distance_to_cluster = haversine(user_input_coords, cluster_coords, unit=Unit.KILOMETERS)
        
        # Check if this cluster is closer than the previous closest one
        if distance_to_cluster < min_distance:
            min_distance = distance_to_cluster
            selected_cluster_coords = cluster_coords  # Update with the coordinates

    # Return a tuple of (latitude, longitude) associated with the selected cluster
    return selected_cluster_coords


waste_transfer_file = "E:\\Berlin-Chapter-Challenge-Waste-Management\\src\\tasks\\task-5-deployment\\pages\\data\\combinedfiles\\waste_transfer_clusters.csv"
recycling_clusters_file = "E:\\Berlin-Chapter-Challenge-Waste-Management\\src\\tasks\\task-5-deployment\\pages\\data\\combinedfiles\\recycling_clusters.csv"

if user_latitude and user_longitude:
    starting_cluster_latitude, starting_cluster_longitude = find_closest_cluster(start_latitude,start_longitude,waste_transfer_file)
    ending_cluster_latitude, ending_cluster_longitude = find_closest_cluster(starting_cluster_latitude,starting_cluster_longitude,recycling_clusters_file)
    url = f'https://api.openrouteservice.org/v2/directions/driving-hgv?api_key={api_key}&start={start_longitude},{start_longitude}&end={ending_cluster_longitude},{ending_cluster_latitude}'
    # Define the headers for the request
    headers = {
        'Accept': 'application/json, application/geo+json',
    }

    # Make the GET request to ORS Directions API
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Parse the API response to extract route data (e.g., latitude and longitude coordinates)
        route_data = response.json()

        # Create a Folium map
        m = folium.Map(location=[start_latitude, start_longitude], zoom_start=10)

        # Add a marker for the start location
        folium.Marker([user_latitude, user_longitude], tooltip="Start").add_to(m)

        # Add a marker for the end location
        folium.Marker([ending_cluster_latitude, ending_cluster_longitude], tooltip="End").add_to(m)
        # Display the Folium map within the Streamlit app
        folium.GeoJson(route_data).add_to(m)
        m.save('route_map.html')
        st.components.v1.html(open("route_map.html").read(), width=800, height=600) 
        
else:
    st.warning("Please enter latitude and longitude coordinates.")