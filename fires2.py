import json

infile = open('US_fires_9_14.json', 'r')


fires = json.load(infile)

list_of_fires = fires
long, lat, brightness = [],[], []
for row in list_of_fires:
    if(row["brightness"]>450):
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

data = [{'type':'scattergeo',
 'lon': long,
 'lat': lat,
 'text': brightness,
 'marker':{
     'size': 8,
     'color': brightness,
     'colorscale': 'Viridis',
     'reversescale': True,
     'colorbar': {'title':'Brightness'}
 }
}
]


my_layout = Layout(title = "Fires greater than 450 from 9/14/20-9/20/20")
fig = {'data':data, 'layout': my_layout}
offline.plot(fig, filename = "firebrightness9.14.html" )