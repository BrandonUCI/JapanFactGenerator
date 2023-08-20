import requests

response = requests.get("https://japan-api.ninja/api/v1/")

print(response.status_code)