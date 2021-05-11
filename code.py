import http.client
import json

conn = http.client.HTTPSConnection("cdn-api.co-vin.in")
payload = ''
headers = {
  'Content-Type': 'application/json'
}
conn.request("GET", "/api/v2/admin/location/states", payload, headers)
res = conn.getresponse()
data = res.read()
data = json.loads(data.decode("utf-8"))
states = data["states"]
# Extracted all the states with their Ids
