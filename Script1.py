__author__ = 'Rachiraju'
import folium

import pandas
df = pandas.read_csv("Volcanoes-USA.txt")

df1 = pandas.read_csv("US_States_Capitals.txt")

def color(elev):
    min = int(df["ELEV"].min())
    step = int((df["ELEV"].max() - df["ELEV"].min())/3)
    if elev in range((min) , (min+step)):
        col = "green"
    elif elev in range((min+step),(min+step+step)):
        col = "orange"
    else:
        col = "red"
    return col



map = folium.Map(location = [37.09024,-95.712891], zoom_start = 6, tiles = "Mapbox bright")

fg = folium.FeatureGroup(name = "Volcano Locations")
fg1 = folium.FeatureGroup(name = "US States and Capitals")

for lat,lon,name,elev in zip(df['LAT'],df["LON"],df["NAME"], df["ELEV"]):
    fg.add_child(folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color=color(elev))))


for lat1,long1,name,capital in zip(df1['latitude'],df1['longitude'],df1['name'],df1['capital']):
    fg1.add_child(folium.Marker(location=[lat1,long1], popup="State: "+ name + ", Capital: "+capital))

map.add_child(fg)
map.add_child(fg1)

map.add_child(folium.GeoJson(data=open("World_Population.json"),
name="World Population",
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005']<= 10000000 else 'orange' if 10000000<x['properties']['POP2005']< 20000000 else 'red'}))

map.add_child(folium.LayerControl() )

map.save(outfile='test.html')