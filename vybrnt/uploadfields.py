import json
import requests

# Load the JSON data from file
with open('fields.json', 'r') as f:
    data = json.load(f)

# # Convert the data back to JSON format
# json_data = json.dumps(data)


# Define the API endpoint and authentication credentials
api_url = 'https://vybrnt1679572212.api-us1.com/api/3/fields'
api_key = 'e6b268a30df8e81bf0aa8702db5647a4e900a23ae421518fb31aaea1f4503557c7408567'

# Set the headers and payload for the API request
headers = {'Api-Token': api_key, 'Content-Type': 'application/json'}
payload = data



for key, item in payload.items():
    # d = f'{{"field":{item}}}'
    d = {}
    d["field"] = item
    print(d)
    #Send the API request to add new fields to the ActiveCampaign account
    response = requests.post(api_url, headers=headers, data=json.dumps(d))
    # Print the response status code and content for debugging
    print(response.status_code)
    print(f"{response.content}\n")

# print(payload)

# #Send the API request to add new fields to the ActiveCampaign account
# response = requests.post(api_url, headers=headers, data=payload)
# # Print the response status code and content for debugging
# print(response.status_code)
# print(f"{response.content}\n")
