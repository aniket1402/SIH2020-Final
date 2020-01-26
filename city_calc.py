from loc import *
from geopy.geocoders import Nominatim
import pprint
geolocator = Nominatim(timeout=10)

(lat,lon) = getLocation()
lat_lon = "{}, {}".format(lat,lon)

def city():
    location = geolocator.reverse(lat_lon)
    addr = location.raw['address']['city']
    # pprint.pprint(addr)
    return addr

print(city())