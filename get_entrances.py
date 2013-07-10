from urllib2 import urlopen
import csv
import simplejson as json

fp = urlopen( "http://www.mta.info/developers/data/nyct/subway/StationEntrances.csv" )

rd = csv.reader( fp )

header_row = rd.next()
hdr = dict(zip(header_row,range(len(header_row))))

features = []
for row in rd:
	geometry = {"type":"Point","coordinates":(row[hdr["Longitude"]],row[hdr["Latitude"]])}

	properties={'marker-color':"#E3BFCB"}
	for i,field in enumerate(header_row):
		if field=="Latitude" or field=="Longitude":
			continue
		properties[field] = row[i]

	feature = {"type":"Feature","properties":properties,"geometry":geometry}
	features.append( feature )

output = {"type":"FeatureCollection","features":features}

fpout = open("station_entrances.geojson","w")
fpout.write( json.dumps(output, indent=2) )
