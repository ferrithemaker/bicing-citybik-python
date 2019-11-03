# bicing-citybik-python

scripts to get real-time Bicing information (Barcelona shared bike service)

#bicing.py :

Gets bicing info of all stations and saves it to influx database (needs influx server *)

Grafana package is recomended to show the logged data

* You can change the database server to log the data if you want

#bicingInfo.py :

Concept demo 

Gets bicing (Barcelona shared bike service) information from citybik API and shows it using tkinter

#bicingAnalytics.py : 

This script uses influx database data generated by bicing.py script

This script creates a csv file with an analysis of station usage ratio. Unbalanced means a regular lack of bikes / free slots

(0% - 50% optimal station) (50% - 75% balanced station) (75% - 100% unbalanced station)

#Resoruces (nov 3 2019):

#Citybik API site :

http://api.citybik.es/v2/

#Grafana docs :

https://grafana.com/docs/

#Influx docs :

https://docs.influxdata.com/influxdb/v1.7/introduction/getting-started/

#Used python3 modules : 

requests | json | influxdb | time | tkinter
