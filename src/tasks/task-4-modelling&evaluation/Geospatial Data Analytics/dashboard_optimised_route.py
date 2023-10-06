import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import pyproj
import warnings

warnings.filterwarnings('ignore')

import folium
import geopandas
from shapely.geometry import Point
from streamlit_folium import st_folium, folium_static
from folium.plugins import MousePosition
from haversine import haversine, Unit

config = {
    'directory_data': 'combinedfiles/',
    'input_file_name': 'station_cluster_centers.csv',
    'output_file_name': 'shortest_path.pkl',
    'clusters_path': 'station_cluster_centers.csv',
    'threshold_in_meters': 500,
    'station_categories': ['waste disposal centres', 'waste transfer stations', 'landfills', 'recycling centres'],
    'germany_map_center': [51.1657, 10.4515],
    'station2color_map': {'waste disposal centres': 'lightblue', 'waste transfer stations': 'gray',
                          'landfills': 'lightred', 'recycling centres': 'lightgreen'},
    'cluster2color_map': {'waste disposal centres': 'darkblue', 'waste transfer stations': 'black',
                          'landfills': 'red', 'recycling centres': 'darkgreen'}
}


def create_point_map(df):
    df['coordinates'] = df[['lat', 'lon']].values.tolist()
    df['coordinates'] = df['coordinates'].apply(Point)
    df = geopandas.GeoDataFrame(df, geometry='coordinates')
    df = df.dropna(subset=['lat', 'lon', 'coordinates'])
    return df


def initial_analysis(df):
    """
        Function to generate EDA chart
    """
    states = df['state'].unique().tolist()
    st.subheader(f"Distribution of number of stations across {len(states)} states")
    statewise_stations = df.groupby(by=['station', 'state']).size().unstack(fill_value=0)
    fig = px.imshow(statewise_stations, width=8000, height=500, text_auto=True, template='seaborn')
    st.plotly_chart(fig, use_container_width=True)
    st.text('This is some interpretation of Figure 1.')

    st.subheader(f"Total Number of Stations")
    total_stations = pd.DataFrame(df.groupby(by=['station', 'state']).size().unstack(fill_value=0).sum(axis=1)).rename(
        columns={0: 'Total'}).reset_index()
    fig = px.bar(total_stations, x='station', y='Total', width=800, height=500, template='seaborn')
    st.plotly_chart(fig, use_container_width=True)
    st.text('This is some interpretation of Figure 2.')


@st.cache_data
def load_preprocess_data(file_1):
    if file_1 is not None:
        filename = file_1.name
        st.write(f"{filename} uploaded successfully")
        df = pd.read_csv(config['directory_data'] + filename)
    else:
        df = pd.read_csv(config['directory_data'] + config['input_file_name'])
        filename = 'station_cluster_centers'

    if 'Unnamed: 0.1' in df.columns.tolist():
        df = df.drop(['Unnamed: 0.1'], axis=1)
    if 'Unnamed: 0' in df.columns.tolist():
        df = df.drop(['Unnamed: 0'], axis=1)

    df.loc[df['state'] == 'Baden_Württemberg', 'state'] = 'Baden-Wurttemberg'
    df.loc[df['state'] == 'Bradenburg', 'state'] = 'Brandenburg'
    df.loc[df['state'] == 'LowerSaxony_Niedersachsen', 'state'] = 'Lower Saxony'
    df.loc[df['state'] == 'Mecklenburg_Vorpommern', 'state'] = 'Mecklenburg-Vorpommern'
    df.loc[df['state'] == 'NorthRhine-Westphalia', 'state'] = 'North Rhine-Westphalia'
    df['lat'] = pd.to_numeric(df['lat'], errors='coerce')
    df['lon'] = pd.to_numeric(df['lon'], errors='coerce')
    st.write(f"{filename} uploaded and preprocessed successfully")
    with st.expander('Preview'):
        st.dataframe(df)

    return df


@st.cache_data(experimental_allow_widgets=True)
def visualise_data(df_orig, plot_label='station2color_map', lat_column='lat', lon_column='lon'):
    """
        Function to visualise all stations and their clusters on folium map
    """
    center = config['germany_map_center']
    zoom_start = 5
    formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
    column1, column2 = st.columns((2))

    df = create_point_map(df_orig)
    map0 = folium.Map(location=center, zoom_start=zoom_start)
    MousePosition().add_to(map0)
    MousePosition(
        position="topright",
        separator=" | ",
        empty_string="NaN",
        lng_first=False,
        num_digits=5,
        prefix="Coordinates:",
        lat_formatter=formatter,
        lng_formatter=formatter).add_to(map0)

    for i, row in df.iterrows():
        icon = folium.Icon(color=config[plot_label][row['station']], size=1)
        folium.Marker([row[lat_column], row[lon_column]], opacity=0.4, icon=icon).add_to(map0)

    st_folium(map0, width=700)


def get_closest_starting_point(clusters_df, coordinates):
    """
        Returns the closest cluster of the
    """
    clusters_df = clusters_df.drop_duplicates(subset=['cluster_ID'])
    point = clusters_df.loc[clusters_df['cluster_ID'] == 0][['cluster_lat', 'cluster_lon']]
    starting_pont = [coordinates['lat'], coordinates['lon']]
    min_distance = haversine(starting_pont, point, unit=Unit.KILOMETERS)
    selected_cluster_id = 0

    for cluster_id in np.unique(clusters_df['cluster_ID']):
        point = clusters_df.loc[clusters_df['cluster_ID'] == cluster_id][['cluster_lat', 'cluster_lon']]
        current_distance = haversine(starting_pont, point, unit=Unit.KILOMETERS)
        if min_distance > current_distance:
            selected_cluster_id = cluster_id
            min_distance = current_distance

    return selected_cluster_id


def get_closest_center_to_cluster(cluster_ID, station, input_data):
    """
        For the given station, returns the closest ID, lat and lon center from the given cluster ID
    """
    subset = input_data.loc[input_data['station'] == station].drop_duplicates(subset=['id'])
    coordinates_cluster_centroid = (float(subset.loc[subset['cluster_ID'] == cluster_ID]['cluster_lat'].values[0]),
                                    float(subset.loc[subset['cluster_ID'] == cluster_ID]['cluster_lon'].values[0]))

    starting_pont = (float(subset.iloc[0]['lat']),
                     float(subset.iloc[0]['lon']))
    selected_center = {'ID': float(subset.iloc[0]['id']),
                       'lat': float(subset.iloc[0]['lat']), 'lon': float(subset.iloc[0]['lon']),
                       'distance': haversine(coordinates_cluster_centroid, starting_pont, unit=Unit.KILOMETERS)}

    for id in np.unique(subset['id']):
        point = (subset.loc[subset['id'] == id]['lat'], subset.loc[subset['id'] == id]['lon'])
        current_distance = haversine(coordinates_cluster_centroid, point, unit=Unit.KILOMETERS)
        if selected_center['distance'] > current_distance:
            selected_center = {'ID': id, 'lat': point[0], 'lon': point[1], 'distance': current_distance}

    return selected_center


def main():
    st.set_page_config(page_title='Task-4-Modelling)', page_icon=':truck:', layout='wide')
    st.title(" Route Optimisation in waste management (Germany)")
    st.markdown('<style>div.block-container{text-align: center}{border:1px solid red}{padding-top:0.5rem;}</style>',
                unsafe_allow_html=True)
    st.text("Description of how route optimisation generally works")
    file_1 = st.file_uploader(":file_folder: Upload the CSV file that contains lat,lon information for all stations",
                              type=['.csv'])
    df = load_preprocess_data(file_1)

    with st.expander('Preview'):
        st.dataframe(df)

    initial_analysis(df)

    coordinates = st.text_input("Kindly Provide the starting point coordinates in the form : latitude, longitude")
    if coordinates is not None and coordinates != '':
        coordinates = {'lat': float(coordinates.split(',')[0].strip()), 'lon': float(coordinates.split(',')[1].strip())}

    stations = st.multiselect("Select the stations for visualisation", df['station'].unique())

    if stations is not None:
        df_2 = df.loc[df['station'].isin(stations)].copy(deep=True)
    else:
        df_2 = df.copy(deep=True)

    column1, column2 = st.columns((2))
    df_2_clusters = df_2.drop_duplicates(subset=['station', 'cluster_ID'])

    with column1:
        visualise_data(df_2, 'station2color_map', 'lat', 'lon')

    with column2:
        visualise_data(df_2_clusters, 'cluster2color_map', 'cluster_lat', 'cluster_lon')

    if coordinates is not None and coordinates != '':
        closest_waste_transfer_station_cluster = get_closest_starting_point(
            df_2_clusters.loc[df_2_clusters['station'] == 'waste transfer stations'], coordinates)

    # Add the code to calculate closest recycling center and the corresponding closest landfill and disposal center (If time is available)
    # From ORS API matrix, get the cluster IDs of closest centers that will lie on our path
    # Final output : closest_waste_transfer_station_cluster , corresponding_closest_recycling_center_cluster
    # Next step : Use function get_closest_center_to_cluster to get the closest station lat , lon
    #             Visualise it in the dashboard

    closest_waste_transfer_station_from_cluster = get_closest_center_to_cluster(closest_waste_transfer_station_cluster,
                                                                                'waste transfer stations', df_2)
    starting_lat, starting_lon, starting_center_ID = closest_waste_transfer_station_from_cluster['lat'], \
                                                     closest_waste_transfer_station_from_cluster['lon'], \
                                                     closest_waste_transfer_station_from_cluster['ID']

    # Similarly write to get recycling center lat lon
    # obj = {}
    # st.download_button("Download generated route.", obj, file_name='shortest_route.pkl')


if __name__ == '__main__':
    main()
