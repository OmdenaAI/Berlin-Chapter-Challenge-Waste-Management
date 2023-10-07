import streamlit as st
import webbrowser
import pandas as pd
import numpy as np
import json 
import pickle 
import requests 
import folium



st.title("Geospatial Data Analytics")
st.write(
                    "Clear and concise route information is presented to users, ensuring they have a comprehensive understanding of selected paths. "
                    "Moreover, users can conveniently download visualizations in .png format, facilitating seamless sharing and integration into various reports and presentations."
                )

st.write("Enter latitude and longitude coordinates to display a map:")

# User Input
user_latitude = st.number_input("Enter Latitude:")
user_longitude = st.number_input("Enter Longitude:")

# Replace with your API key
api_key = "5b3ce3597851110001cf62481812d7fb40e0470695b078ee763d603e"

# Replace with your specific latitude and longitude coordinates for the starting and ending points
start_latitude = user_latitude
start_longitude = user_longitude
waste_transfer_lat = 0
waste_transfer_lon = 0
recycling_lat = 49.420318
recycling_lon = 8.687872


if latitude and longitude:
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