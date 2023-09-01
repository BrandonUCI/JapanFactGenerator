import requests

def apiCall()->list:
    """ Makes a call to the API and returns a list of prefecture dictionaries.
    List Schema:
    [{'id': int, 'name': str, 'iso2': str}, ...]
    """
    # API Link
    url = "https://api.countrystatecity.in/v1/countries/JP/states"

    # API Key
    headers = {'X-CSCAPI-KEY': 'aW4zVHd1WkFuTWcyWURQRnpvTTgxTFU5d05sV3VLdzhhbGxpWEk4YQ=='}

    # API call request
    response = requests.request("GET", url, headers=headers)
    data = None

    # If request is successful
    if response.status_code == 200: 
        # Convert response content to dictionary
        return response.json()  
    # If unexpected response
    else:
        print("Request failed with status code:", response.status_code)

def generateFact(prefecture: str)->str:
    """Takes in a prefecture and returns a fun fact about the prefecture"""
    return "generateFact WIP"
    


if __name__ == '__main__':
    apiData = apiCall()
    print(apiData)
    for prefecture in apiData:
        print(prefecture)