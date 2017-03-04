import overpy
import csv

api = overpy.Overpass()

with open("query.oql") as oql:
    result = api.query(oql.read())

ofile = open("output.csv", "w")
csvfile = csv.writer(ofile)

for way in result.ways:
    csvfile.writerow((way.tags.get("name"), way.center_lat, way.center_lon))

for node in result.nodes:
    csvfile.writerow((way.tags.get("name"), node.lat, node.lon))
