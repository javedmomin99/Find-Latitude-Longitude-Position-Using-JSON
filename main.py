import requests

response= requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
#data = response.json()["iss_position"]
#data = response.json()["timestamp"]
#data = response.json()["message"]
latitude = response.json()["iss_position"]["latitude"]
longitude = response.json()["iss_position"]["longitude"]
iss_position = latitude,longitude
print(f"latitude = {iss_position[0]},\nlongitude = {iss_position[1]}" )