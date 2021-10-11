import json

infile = open('US_fires_9_1.json', 'r')
outfile = open('readable_fire data.json', 'w')

fires = json.load(infile)

list_of_fires = fires
long, lat, brightness = [],[], []
for row in list_of_fires:
    longtitude = row["longitude"]
    long.append(longtitude)
    latitude = row["latitude"]
    lat.append(latitude)
    bright = row["brightness"]
    brightness.append(bright)

print(long[:5])
print(lat[:5])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{'type': 'scattergeo',
'lon':long, 
'lat':lat,
'marker':{
    'size': [5*b for b in brightness],
    'color':brightness,
    'colorscale':'Virdis',
    'reversecale': True,
    'colorbar':{'title':'Brightness'}
}}]

my_layout = Layout(title = "Fire brightness")
fig = {'data':data, 'layout': my_layout}
offline.plot(fig, filename = "firebrightness9.1.html" )