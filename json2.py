import json

infile = open('eq_data_30_day_m1.json', 'r')
outfile = open('readable_eq data.json', 'w')

eqdata = json.load(infile)

json.dump(eqdata,outfile,indent = 4)

print(eqdata["features"][0]["properties"]["mag"])

list_of_eqs = eqdata["features"]

mags, lat, long, hover_text = [],[],[],[]
for row in list_of_eqs:
    mag = row["properties"]["mag"]
    mags.append(mag)
    longtitude = row["geometry"]["coordinates"][0]
    long.append(longtitude)
    latitude = row["geometry"]["coordinates"][1]
    lat.append(latitude)
    text = row["properties"]["title"]
    hover_text.append(text)

#list slicing
print(mags[0:5])
print(long[:5])
print(lat[:5])

from plotly.graph_objs import Scattergeo, Layout 
from plotly import offline

#minimum needed
#data = [Scattergeo(lon = long, lat = lat)]
data = [{'type':'scattergeo',
 'lon': long,
 'lat': lat,
 'text': hover_text,
 'marker':{
     'size': [5*m for m in mags],
     'color': mags,
     'colorscale': 'Viridis',
     'reversescale': True,
     'colorbar': {'title':'Magnitude'}
 }
}
]
my_layout = Layout(title = "Global Earthquakes 30 Day")
fig = {'data':data, 'layout': my_layout}
offline.plot(fig, filename = "globalearthquakesday30.html" )
