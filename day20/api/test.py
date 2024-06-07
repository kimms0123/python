import requests

lat = 37.491
lon = 126.72
apikey = "5a30b7c2563613f6703a0b690378b764"
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}"

response = requests.get(url)
data = response.json()
print(data)