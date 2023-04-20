import requests
import json


# Set up authentication credentials
api_key = '77cb98527763da722c1fa622b65099c74a6742c57d2d4b1e3175c50a0873dec58bd7e0b4'
api_url = 'https://lendconnectsandbox.api-us1.com/api/3/'

# Define the API endpoint for retrieving the custom object schema
endpoint = api_url + 'customObjects/schemas'

# Send the API request to retrieve the custom object schema
response = requests.get(endpoint, headers={'Api-Token': api_key})

# Parse the API response
custom_object_schema = json.loads(response.text)

# Print the custom object schema with formatted JSON output
print(json.dumps(custom_object_schema, indent=2))
