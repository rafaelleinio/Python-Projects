import pandas
import time
from geopy import geocoders
from geopy.exc import GeocoderTimedOut

df1 = pandas.read_excel("parse_addres.xlsx")
g = geocoders.GoogleV3(api_key="AIzaSyDZy6kWX8oN-pT96HqzgdSBNtJJSzc5cx8")

def do_geocode(address):
	try:
		return g.geocode(address,timeout=10)
	except GeocoderTimedOut:
		print "TIME OUT"
		return do_geocode(address)

for i, row in df1.iterrows():
	address = row["string"]
	location = do_geocode(address)
	if location is not None:
		street_number=""
		route=""
		neighborhood=""
		city=""
		state="";
		zipcode=""
		for component in location.raw['address_components']:
		    if component['types'][0] =="street_number":
		        street_number = component['short_name']
		    elif component['types'][0]=="route":
		        route = component['short_name']
		    elif component['types'][0]=="political":
		        neighborhood = component['short_name']
		    elif component['types'][0]=="administrative_area_level_2":
		        city = component['short_name']
		    elif component['types'][0]=="administrative_area_level_1":
		        state = component['short_name']
		    elif component['types'][0]=="postal_code":
		        zipcode = component['short_name']
		df1["state"][i] = state
		df1["city"][i] = city
		df1["address"][i] = route +', '+street_number
		df1["neighborhood"][i] = neighborhood
		df1["zipcode"][i] = zipcode
		df1["lat"][i] = location.latitude
		df1["lng"][i] = location.longitude	
		df1["enabled"][i]= "TRUE"
		df1["name"][i] = "Polo " + df1["neighborhood"][i] + " " +df1["city"][i] + " - " + df1["state"][i]
	time.sleep(0.1)
	print(i)
df1.to_excel("parse_addres.xlsx")