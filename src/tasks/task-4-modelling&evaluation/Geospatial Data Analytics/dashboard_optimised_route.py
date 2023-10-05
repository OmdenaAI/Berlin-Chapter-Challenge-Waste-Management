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


config = {
    'directory_data': 'Geospatial Data Analytics/combinedfiles/',
    'without_factors_geospatial_data_path': 'Geospatial Data Analytics/combinedfiles/complete_geospatialdata_withoutfactors.csv',
    'clusters_path': '',
    'threshold_in_meters': 500,
    'station_categories': ['waste disposal centres', 'waste transfer stations', 'landfills', 'recycling centres'],
    'germany_map_center' : [51.1657, 10.4515],
    'station2color_map': {'waste disposal centres': 'blue', 'waste transfer stations': 'black', 'landfills':'red', 'recycling centres':'green'}
}

def project_latlon_to_utm(row, utm_proj):
    lat = row['lat']
    lon = row['lon']
    x, y = utm_proj(lon, lat)
    return x, y

def convert_utm_to_latlon(row, utm_proj):
    x = row['x']
    y = row['y']
    lon, lat = utm_proj(x, y, inverse=True)
    return lat, lon

def group_points_by_proximity(df_orig, threshold):
    df_orig = df_orig.copy(deep=True)
    df_orig[['x', 'y']] = np.nan
    utm_zone = '33'
    utm_proj = pyproj.Proj(proj='utm', zone=utm_zone, ellps='WGS84')
    print(len(df_orig))
    df_orig[['x', 'y']] = df_orig.apply(lambda row: project_latlon_to_utm(row, utm_proj), axis=1).tolist()

    final_df = pd.DataFrame()
    for station in df_orig['station'].unique():
        df = df_orig.loc[df_orig['station']==station]
        lat_grid_cells = int((df['y'].max() - df['y'].min()) / threshold) + 1
        lon_grid_cells = int((df['x'].max() - df['x'].min()) / threshold) + 1
        df['lat_idx'] = ((df['y'] - df['y'].min()) / threshold).astype(int)
        df['lon_idx'] = ((df['x'] - df['x'].min()) / threshold).astype(int)
        df['group'] = df['lat_idx'] * lon_grid_cells + df['lon_idx']
        df.drop(['lat_idx', 'lon_idx'], axis=1, inplace=True)
        centroids = df.groupby(by = ['group']).mean()[['x', 'y']].reset_index()
        centroids.rename(columns={'y': 'centroid_y', 'x': 'centroid_x'}, inplace=True)
        df = pd.merge(df, centroids, on='group', how='left')
        final_df = pd.concat([final_df, df])
        print(f"Len === {len(final_df)}, {centroids['group'].nunique()}")
    final_df[['centroid_lat', 'centroid_lon']] = final_df.apply(lambda row: convert_utm_to_latlon(row, utm_proj), axis=1).tolist()
    return final_df


def initial_analysis(df):
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
        df = pd.read_csv(config['without_factors_geospatial_data_path'])
        filename = 'without_factors_geospatial_data_path'

    if 'Unnamed: 0.1' in df.columns.tolist():
        df = df.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1)
    df.loc[df['state'] == 'Baden_Württemberg', 'state'] = 'Baden-Wurttemberg'
    df.loc[df['state'] == 'Bradenburg', 'state'] = 'Brandenburg'
    df.loc[df['state'] == 'LowerSaxony_Niedersachsen', 'state'] = 'Lower Saxony'
    df.loc[df['state'] == 'Mecklenburg_Vorpommern', 'state'] = 'Mecklenburg-Vorpommern'
    df.loc[df['state'] == 'NorthRhine-Westphalia', 'state'] = 'North Rhine-Westphalia'
    df['lat'] = pd.to_numeric(df['lat'], errors='coerce')
    df['lon'] = pd.to_numeric(df['lon'], errors='coerce')
    df = df.sample(n=200)
    st.write(f"{filename} uploaded and preprocessed successfully")
    with st.expander('Preview'):
        st.dataframe(df)
    return df


def create_point_map(df):
    df['coordinates'] = df[['lat', 'lon']].values.tolist()
    df['coordinates'] = df['coordinates'].apply(Point)
    df = geopandas.GeoDataFrame(df, geometry='coordinates')
    df = df.dropna(subset=['lat', 'lon', 'coordinates'])
    return df


@st.cache_data(experimental_allow_widgets=True)
def visualise_data(df):
    df = create_point_map(df)
    center = config['germany_map_center']
    zoom_start = -1
    tile_1 = 'Mapbox Bright'
    map = folium.Map(location=center, zoom_start=zoom_start)
    MousePosition().add_to(map)
    formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"

    MousePosition(
        position="topright",
        separator=" | ",
        empty_string="NaN",
        lng_first=False,
        num_digits=5,
        prefix="Coordinates:",
        lat_formatter=formatter,
        lng_formatter=formatter,
    ).add_to(map)

    for i, row in df.iterrows():
        icon = folium.Icon(color=config['station2color_map'][row['station']], size=1)
        folium.Marker([row['lat'], row['lon']], opacity=0.4, icon=icon).add_to(map)
    # folium_static(map, width=700)
    st_folium(map, width = 700)


def main():
    # Set Page Title
    st.set_page_config(page_title='Task-4-Modelling)', page_icon=':truck:', layout='wide')
    st.title(" Route Optimisation in waste management (Germany)")
    st.markdown('<style>div.block-container{text-align: center}{border:1px solid red}{padding-top:0.5rem;}</style>', unsafe_allow_html=True)
    st.text("Description of how route optimisation generally works")
    file_1 = st.file_uploader(":file_folder: Upload the CSV file that contains lat,lon information for all stations", type=['.csv'])
    df = load_preprocess_data(file_1)

    with st.expander('Preview'):
        st.dataframe(df)

    initial_analysis(df)
    stations = st.multiselect("Select the stations for visualisation", df['station'].unique())

    if stations is not None:
        df_2 = df.loc[df['station'].isin(stations)].copy(deep=True)
    else:
        df_2 = df.copy(deep=True)

    visualise_data(df_2)


if __name__ == '__main__':
    main()
