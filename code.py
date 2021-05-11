import http.client
import json
import time
from datetime import date
def RequestDataFromAPI(url):
  conn = http.client.HTTPSConnection("cdn-api.co-vin.in")
  payload = ''
  headers = {
    'Content-Type': 'application/json'
  }
  conn.request("GET", url, payload, headers)
  res = conn.getresponse()
  data = res.read()
  try:
    data = json.loads(data.decode("utf-8"))
  except:
    data = {}
  return data

# Extracted all the states with their Ids
url = "/api/v2/admin/location/states"
data = RequestDataFromAPI(url)
states = data["states"]

# Extracted all the districts with their Ids
#[state, stateID, district,districtID]
districts = []
for state in states:
  stateid = state['state_id']
  url = "/api/v2/admin/location/districts/"+str(stateid)
  districtData = RequestDataFromAPI(url)
  districtData = districtData['districts']
  for d in districtData:
    dis = [ state['state_name'], stateid, d['district_name'], d['district_id']]
    districts.append(dis)

dateToday = date.today()
date = str(dateToday.day+5)+"-"+str(dateToday.month)+"-"+str(dateToday.year)
for district in districts:
  # print(district)
  districtId = district[3]
  # url = "/api/v2/appointment/sessions/public/findByDistrict?district_id="+str(districtId)+"&date="+str(date)
  # districtData = RequestDataFromAPI(url)
  print(district)

# dateToday = date.today()
# date = str(dateToday.day+5)+"-"+str(dateToday.month)+"-"+str(dateToday.year)
# print(len(districts),len(states))

