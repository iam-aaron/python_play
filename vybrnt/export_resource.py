import requests
import json

# Set API URL and key
api_url = "https://molliesandbox.api-us1.com/api/3/"
api_key = "8994156a780baf112241c542649e73422f96aea46399dd0fcf3f92d12bb49241bab57f96"

# Define resource endpoints
endpoints = ["contacts", "deals", "companies", "tasks", "notes"]

# Loop through each endpoint and export data
for endpoint in endpoints:
    # Set endpoint URL
    url = api_url + endpoint
    
    # Set headers and parameters for the API request
    headers = {"Api-Token": api_key}
    params = {"limit": 1000} # adjust limit as needed
    
    # Make API request
    response = requests.get(url, headers=headers, params=params)
    
    # Convert JSON response to Python dict
    data = json.loads(response.text)
    
    # Write data to file
    with open(endpoint + ".json", "w") as outfile:
        json.dump(data, outfile, indent=4)