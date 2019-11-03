# gets bicing info of all stations and saves it to influx database (needs influx server) 
# grafana package is recomended to show the logged data
# created by FerriTheMaker using citybik API

from influxdb import InfluxDBClient
import time
import json
import requests

# wait to start influx (for rc.local)
time.sleep(20)
# Influx setup
influxclient = InfluxDBClient(host='localhost', port=8086)
influxclient.switch_database('bicing')

try:
	while True:
		r = requests.get('http://api.citybik.es/v2/networks/bicing')
        	#print(bicingJson['network']['stations'])
		bicingJson = r.json()
		for station in bicingJson['network']['stations']:
			address = str(station['name'])
			bikes = int(station['free_bikes'])
			slots = int(station['empty_slots'])
			id = str(station['id'])
			json_insert = [ { "measurement" : "bicing_accounting", "tags" : { "id": id, "address" : address }, "fields" : { "bikes" : bikes, "slots" : slots } } ]
			influxclient.write_points(json_insert)
		time.sleep(300)
except KeyboardInterrupt:
	print("bye")
