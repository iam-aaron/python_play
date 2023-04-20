import requests
import json

# Set up authentication credentials
api_key = '77cb98527763da722c1fa622b65099c74a6742c57d2d4b1e3175c50a0873dec58bd7e0b4'
api_url = 'https://lendconnectsandbox.api-us1.com/api/3/'

# Define the API endpoint for retrieving fields
endpoint = api_url + 'fields'

# Send the API request to retrieve the fields
response = requests.get(endpoint, headers={'Api-Token': api_key})

# Parse the API response
fields_data = json.loads(response.text)['fields']

# Loop through the fields and print their group information
for field_data in fields_data:
    field_id = field_data['id']
    field_title = field_data['title']
    group_ids = field_data.get('groups', [])
    groups_info = []

    # Retrieve the group information for each group ID
    for group_id in group_ids:
        group_endpoint = api_url + f'groups/{group_id}'
        group_response = requests.get(group_endpoint, headers={'Api-Token': api_key})

        # Handle errors if group is not found
        if group_response.status_code == 404:
            groups_info.append({'id': group_id, 'name': 'Not found'})
        else:
            group_data = json.loads(group_response.text)['group']
            groups_info.append({'id': group_id, 'name': group_data['name']})

    # Print the field information
    print(f"Field ID: {field_id}\nTitle: {field_title}\nGroups: {groups_info}\n")
