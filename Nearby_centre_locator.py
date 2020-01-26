import requests
import pprint
import time
import googlemaps
from loc import *
# Make the FIRST request for the IP Address.
# ip_request = requests.get(url = 'https://get.geojs.io/v1/ip.json')

# # Grab the IP Address.
# my_ip = ip_request.json()['ip']

# # Make the SECOND request for the GeoLocation.
# geo_request_url = 'https://get.geojs.io/v1/ip/geo/{}.json'.format(my_ip)
# geo_data = requests.get(url = geo_request_url).json()

# Grab the Latitutde & Longitude.
# lat = geo_data['latitude']
# lon = geo_data['longitude']


# # Print all the data.
# print(geo_data)

(lat,lon)=getLocation()

# Print it so you can read just the Lat/Lon.
print('{},{}'.format(lat, lon))

# Google Map Lat/Lon Format
gmap_lat_lon = '{},{}'.format(lat, lon)

# You could also store it as a Tuple.
# gmap_lat_lon = (lat,lon)

# You could also store it as a Dictionary.
# gmap_lat_lon = {"lat":lat,"lng":lon}

# Create a new instance of the GMAP Client.
gmaps=googlemaps.Client(key = "apikey")

# Make a request for some places.
places_result = gmaps.places_nearby(location = gmap_lat_lon, radius = 40000, open_now = True, type = 'hospital')

# Print the results.
pprint.pprint(places_result)