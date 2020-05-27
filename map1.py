import folium
import pandas

data = pandas.read_csv("city.csv")
Lat = list(data["Lat"])
Lon = list(data["Long"])
map = folium.Map(location =[25.59, 85.12],zoom_start=6)
fg = folium.FeatureGroup(name="My map")
for lt, ln in zip(Lat,Lon):
    fg.add_child(folium.Marker(location=[lt,ln],popup="Red zone",icon=folium.Icon(color="red")))
map.add_child(fg)
map.save("Map1.html")
