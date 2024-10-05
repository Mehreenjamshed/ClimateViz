# map_project.py

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests
import cartopy.crs as ccrs
from ipyleaflet import Map, WMSLayer, Marker, Popup, LayersControl
from ipywidgets import HTML

# Define the WMS URL
wms_url = 'https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi?'

# Create a WMS Layer for thermal anomalies
wms_layer = WMSLayer(
    url=wms_url,
    layers='VIIRS_NOAA20_Thermal_Anomalies_375m_All',
    format='image/png',
    transparent=True
)

# Create the interactive map
m = Map(basemap=basemaps.NASAGIBS.BlueMarble, center=(0, 0), zoom=3)
m.add_layer(wms_layer)

# Function to create a marker with a popup
def create_marker(location, message):
    marker = Marker(location=location)
    popup = Popup(location=location, child=HTML(value=message), close_button=True)
    marker.popup = popup  # Attach the popup to the marker
    return marker

# Create markers for different locations with HTML messages
new_york_marker = create_marker((40.7128, -74.0060), "<h3>Welcome to New York City!</h3>")
los_angeles_marker = create_marker((34.0522, -118.2437), "<h3>Welcome to Los Angeles!</h3>")
chicago_marker = create_marker((41.8781, -87.6298), "<h3>Welcome to Chicago!</h3>")

# Add markers to the map
m.add_layer(new_york_marker)
m.add_layer(los_angeles_marker)
m.add_layer(chicago_marker)

# Add layer control to toggle between basemaps
layer_control = LayersControl()
m.add_control(layer_control)

# Display the updated map
m
