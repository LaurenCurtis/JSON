import json

infile = open('eq_data_30_day_m1.json', 'r')
outfile = open('readable_eq data.json', 'w')

eqdata = json.load(infile)

json.dump(eqdata,outfile,indent = 4)

print(eqdata["features"][0]["properties"]["mag"])

list_of_eqs = eqdata["features"]
mags = []
long = []
lat = []
for row in list_of_eqs:
    mag = row["properties"]["mag"]
    mags.append(mag)
    longtitude = row["geometry"]["coordinates"][0]
    long.append(longtitude)
    latitude = row["geometry"]["coordinates"][1]
    lat.append(latitude)

#list slicing
print(mags[0:5])
print(long[:5])
print(lat[:5])

from plotly.graph_objs import Scattergeo, Layout 
from plotly import offline


data = [Scattergeo(lon = long, lat = lat)]
my_layout = Layout(title = "Global Earthquakes 1 Day")
fig = {'data':data, 'layout': my_layout}
offline.plot(fig, filename = "globalearthquakesday1.html" )
