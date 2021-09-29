import json

infile = open('eq_data_1_day_m1.json', 'r')
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
    longtitude = row["geometry"]["coordinates"][1]
    long.append(longtitude)
    latitude = row["geometry"]["coordinates"][0]
    lat.append(latitude)


print(mags)
print(long)
print(lat)

