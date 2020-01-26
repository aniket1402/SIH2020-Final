from loc import *
from kivy.garden.mapview import MapView, MapMarker
from kivy.app import App

(lat, lon) = getLocation()

class MapViewApp(App):
    def build(self):
        mapview = MapView(zoom=16, lat=lat, lon=lon)
        m1 = MapMarker(lon=lon, lat=lat)
        mapview.add_marker(m1)
        return mapview

MapViewApp().run()