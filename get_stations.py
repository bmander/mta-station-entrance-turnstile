from urllib2 import urlopen
import zipfile
from StringIO import StringIO
import csv
import simplejson as json

fp = urlopen("http://www.mta.info/developers/data/nyct/subway/google_transit.zip")
ss = StringIO()
ss.write( fp.read() )
ss.seek(0)
zf = zipfile.ZipFile( ss )
stops = zf.open( "stops.txt" )

rd = csv.reader( stops )
header_row = rd.next()
print header_row
hdr = dict(zip(header_row,range(len(header_row))))

features = []
for row in rd:
	geometry = {"type":"Point","coordinates":(row[hdr["stop_lon"]],row[hdr["stop_lat"]])}

	properties={}
	for i,field in enumerate(header_row):
		if field=="stop_lat" or field=="stop_lon":
			continue
		properties[field] = row[i]

	feature = {"type":"Feature","properties":properties,"geometry":geometry}
	features.append( feature )

output = {"type":"FeatureCollection","features":features}

fpout = open("stations.geojson","w")
fpout.write( json.dumps(output, indent=2) )

for row in rd:
	print row
	exit()
