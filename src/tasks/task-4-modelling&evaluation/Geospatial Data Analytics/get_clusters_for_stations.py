import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import pyproj
import warnings
warnings.filterwarnings('ignore')
from haversine import haversine, Unit
import os

config = {
    'directory_data': 'combinedfiles/',
    'input_file_name': 'complete_geospatialdata_withoutfactors.csv',
    'output_file_name': 'station_cluster_centers.csv',
    'optimal_num_clusters': {
        'waste disposal centres': 20,
        'waste transfer stations': 20,
        'landfills': 20,
        'recycling centres': 21
    },
    'threshold_in_meters': 500,
    'station_categories': ['waste disposal centres', 'waste transfer stations', 'landfills', 'recycling centres'],
}


def project_latlon_to_utm(row, utm_proj):
    """
        Function to convert latitude and longitude into x, y coordinates based on UTM projection
    :param row: a dictionary with 'lat' and 'lon' keys
    :param utm_proj: UTM projection object for a specific zone
    :return: x and y coordinates
    """

    lat = row['lat']
    lon = row['lon']
    x, y = utm_proj(lon, lat)
    return x, y

def convert_utm_to_latlon(row, utm_proj):
    """
        Function to convert x, y coordinates into latitude and longitude based on UTM projection
    :param row: a dictionary with 'x' and 'y' keys
    :param utm_proj: UTM projection object for a specific zone
    :return: x and y coordinates
    """
    x = row['x']
    y = row['y']
    lon, lat = utm_proj(x, y, inverse=True)
    return lat, lon


def group_points_by_proximity(df_orig, threshold):
    """
        Funtion to group lat, lon values from unique stations within a threshold x threshold grid together to remove duplicates
        df_orig (Dataframe) : Pandas Dataframe with 'lat' and 'lon' column
        threshold (int): Grid size in meters
    :return:
        final_df (Dataframe): Processed Dataframe with added columns : 'group', 'centroid_lat', 'centroid_lon'
        'centroid_x', 'centroid_y' for each entry

    """

    df_orig = df_orig.copy(deep=True)
    df_orig[['x', 'y']] = np.nan
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
        centroids = df.groupby(by=['group'])[['x', 'y']].mean().reset_index()
        centroids.rename(columns={'y': 'centroid_y', 'x': 'centroid_x'}, inplace=True)
        df = pd.merge(df, centroids, on='group', how='left')
        final_df = pd.concat([final_df, df])
    final_df[['centroid_lat', 'centroid_lon']] = final_df.apply(lambda row: convert_utm_to_latlon(row, utm_proj), axis=1).tolist()
    return final_df


def load_input_data(path, threshold):
    """
        Main fynction to load and process dataframe: Correct state name, replace duplicated entries with their centroid lat and lon, generate clusters
        for each station and save it in the data directory
    """

    df = pd.read_csv(path)
    stations = config['station_categories']
    if 'Unnamed: 0.1' in df.columns.tolist():
        df = df.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1)
    df.loc[df['state']=='Baden_Württemberg', 'state'] = 'Baden-Wurttemberg'
    df.loc[df['state']=='Bradenburg', 'state'] = 'Brandenburg'
    df.loc[df['state']=='LowerSaxony_Niedersachsen', 'state'] = 'Lower Saxony'
    df.loc[df['state']=='Mecklenburg_Vorpommern', 'state'] = 'Mecklenburg-Vorpommern'
    df.loc[df['state']=='NorthRhine-Westphalia', 'state'] = 'North Rhine-Westphalia'
    df['group'] = np.nan

    print(f'\n----- File with lat, lon data for all stations inside germany read and preprocessed successfully ---\n')
    orig_len = len(df)
    print(f"Total Unique states : {len(df['state'].unique())}")
    print(f"Original Rows in df : {orig_len}")

    for station in stations:
        print(f"| Station : {station} , Number of entries : {len(df.loc[df['station'] == station])}")

    df = df.drop_duplicates(subset=['station', 'lat', 'lon'])
    df_removed = group_points_by_proximity(df, 	threshold)
    print(f"Unique groups : {df_removed['group'].nunique()}")

    df_removed = df_removed.drop_duplicates(subset=['station', 'group'])
    df_removed.to_csv(config['directory_data'] + f'{threshold}m_geospatial_duplicates_removed.csv')
    print(f'\n ----- File Saved After removing duplicates within a distance of {threshold} m \n')

    for station in stations:
        print(f"| Station : {station} , Number of entries : {len(df_removed.loc[df_removed['station'] == station])}")

    return df_removed


def kmeans_clustering(df_subset, station, optimal_num_clusters):
    """
        K-means clustering algorithm implemented to generate cluser id and cluster center for each entry
    :param df_subset:
    :param station:
    :param optimal_num_clusters:
    :return:
    """
    kmeans = KMeans(n_clusters=optimal_num_clusters, random_state=0)
    df_subset['cluster_ID'] = kmeans.fit_predict(df_subset[['centroid_x', 'centroid_y']])
    cluster_centers = kmeans.cluster_centers_

    df_subset['x'] = df_subset.apply(lambda row : cluster_centers[row['cluster_ID']][0], axis=1)
    df_subset['y'] = df_subset.apply(lambda row : cluster_centers[row['cluster_ID']][1], axis=1)
    df_subset[['cluster_lat', 'cluster_lon']] = df_subset.apply(lambda row: convert_utm_to_latlon(row, utm_proj), axis=1).tolist()
    print(f" -- {station} | #Clusters: {optimal_num_clusters} --")
    return df_subset


def get_clusters_for_stations(df):
    df_removed = df.copy(deep=True).drop_duplicates(subset=['station', 'group']).drop(['x', 'y'], axis=1)
    disposal_centers = df_removed.loc[df_removed['station'] == 'waste disposal centres']
    transfer_centers = df_removed.loc[df_removed['station'] == 'waste transfer stations']
    landfills = df_removed.loc[df_removed['station'] == 'landfills']
    recycle_centers = df_removed.loc[df_removed['station'] == 'recycling centres']

    disposal_centers = kmeans_clustering(disposal_centers, 'waste disposal centres', config['optimal_num_clusters']['waste disposal centres'])
    transfer_centers = kmeans_clustering(transfer_centers, 'waste transfer stations', config['optimal_num_clusters']['waste transfer stations'])
    landfills = kmeans_clustering(landfills, 'landfills', config['optimal_num_clusters']['landfills'])
    recycle_centers = kmeans_clustering(recycle_centers, 'recycling centres', config['optimal_num_clusters']['recycling centres'])
    cluster_centers = pd.concat([disposal_centers, transfer_centers, landfills, recycle_centers]).drop(['group', 'centroid_x', 'centroid_y', 'x', 'y'], axis=1)
    cluster_centers = cluster_centers[['id', 'state', 'station', 'lat', 'lon', 'cluster_lat', 'cluster_lon', 'cluster_ID']]

    cluster_centers.to_csv(config['directory_data'] + config['output_file_name'])
    return cluster_centers


if __name__ == '__main__':
    utm_zone = '33'
    utm_proj = pyproj.Proj(proj='utm', zone=utm_zone, ellps='WGS84')
    print(os.getcwd())
    df_removed_duplicates = load_input_data(config['directory_data'] + config['input_file_name'], threshold=config['threshold_in_meters'])
    cluster_centers = get_clusters_for_stations(df_removed_duplicates)