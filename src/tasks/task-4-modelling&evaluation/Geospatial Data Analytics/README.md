Download shapefiles for Germany's Road Network from [here](https://mapcruzin.com/free-germany-arcgis-maps-shapefiles.htm)

Drive link for germany_highwaysandmajorroads[here](https://drive.google.com/drive/folders/10q6jFNqJKQo9u-Mjaik9yfC2awVdqMZy?usp=sharing)

# Route Optimisation Modelling

# Data files - combined files. 

Contains combiend file of various waste centres for all states of germany. 
- Complete_geospatialdata_withoutfactors.csv file is the main file for our modelling. It contains id , longitude , latitude , state , station for each of the centres for each state in Germany. 
- without factors means that the file contains no information regarding the categories related to recycling centres. 
- rest of the files were used to create the above file using the code in Kavita-work.ipynb

# Model.ipynb

- This file contains code for fetching the routes and direction matrix using ORS API and optimising it. 

- route_data.geojson file is the output file from the model.ipynb

- route_map.html is the visualisation of the route_data.geojson file using folium. 

