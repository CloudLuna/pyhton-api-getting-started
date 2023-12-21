import requests
import json
#To retrieve data: GET
#This example don´t require parameters
response = requests.get("http://api.open-notify.org/astros.json")

#Show 200 if is all ok, and an error  if there's a problem                        
print("\nSHOW STATUS OF REQUEST:")
print(response.status_code)

#print the data
print("SHOW RAW DATA REQUESTED")
print(response.json())
#print it in json format
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
print("SHOW DATA IN JSON FORMAT")
jprint(response.json())

#Retrieve data that require parameters (most of API required parameters)
#the same than doing https://api.open-notify.org/iss-pass.json?lat=40.71&lon;=-74 is using
#params option:
parameters = {
    "lat": 40.71,
    "lon": -74
}
#response = requests.get("https://api.open-notify.org/iss-pass.json", params=parameters)
#jprint(response.json())
pass_t=response.json()['people']
jprint(pass_t)
#extract just names:
names = []
for n in pass_t:
    name_n = n['name']
    names.append(name_n)

print(names)
