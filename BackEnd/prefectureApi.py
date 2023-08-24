import requests
import pprint
url = "https://api.countrystatecity.in/v1/countries/JP/states"

headers = {
  'X-CSCAPI-KEY': 'aW4zVHd1WkFuTWcyWURQRnpvTTgxTFU5d05sV3VLdzhhbGxpWEk4YQ=='
}

response = requests.request("GET", url, headers=headers)
data = None

if response.status_code == 200:  # Check if the request was successful
    data = response.json()  # Convert response content to dictionary
    for prefecture in data:
        print(prefecture)
else:
    print("Request failed with status code:", response.status_code)
    
print(type(data))



def generateFact(prefecture: str)->str:
    """Takes in a prefecture and returns a fun fact about the prefecture"""
    pass