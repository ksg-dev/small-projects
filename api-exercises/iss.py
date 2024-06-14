import requests

# request to ISS server, save to variable
response = requests.get(url="http://api.open-notify.org/iss-now.json")

# Instead use requests module
response.raise_for_status()

# get actual data
longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
