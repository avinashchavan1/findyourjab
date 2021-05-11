import http.client
import json
import time

def RequestDataFromAPI(url):
  conn = http.client.HTTPSConnection("cdn-api.co-vin.in")
  payload = ''
  headers = {
    'Content-Type': 'application/json'
  }
  conn.request("GET", url, payload, headers)
  res = conn.getresponse()
  data = res.read()
  data = json.loads(data.decode("utf-8"))
  return data


url = "/api/v2/admin/location/states"
data = RequestDataFromAPI(url)

states = data["states"]
# Extracted all the states with their Ids
district = {}
for state in states:
  stateid = state['state_id']
  url = "/api/v2/admin/location/districts/"+str(stateid)
  districtData = RequestDataFromAPI(url)
  districtData = districtData['districts']
  district[stateid] = districtData

