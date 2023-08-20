import requests

response = requests.get("https://api.countrystatecity.in/v1/countries")

print(response.status_code)