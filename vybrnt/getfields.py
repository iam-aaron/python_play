import requests
import json
import re

def format_fields_as_json(fields):
    formatted_fields = {}
    ctr = 0
    for field in fields:
        # formatted_field = {
        #     "id": field["id"],
        #     "name": field["title"],
        #     "type": field["type"],
        #     "options": field["options"] if "options" in field else []
        # }
        formatted_field = {
            "title": field["title"],
            "type": field["type"],
            "visible": field["visible"],
            "ordernum": field["ordernum"],
            "isrequired": field["isrequired"],
            "show_in_list": field["show_in_list"],
            "defval": field["defval"],
            "relations": field["relations"],
            "links": field["links"],
            "perstag": field["perstag"],
            "rows": field["rows"],
            "cols": field["cols"],
            "service": field["service"],
            "ordernum": field["ordernum"],
            "id": field["id"],
            "options": field["options"] if "options" in field else []
        }
        # formatted_fields.append(formatted_field)
        formatted_fields["field"+str(ctr)] = formatted_field
        ctr += 1
    
    data = json.dumps(formatted_fields, indent=4)
    data = re.sub('\[\n {7}', '[', data)
    data = re.sub('(?<!\]),\n {7}', ',', data)
    data = re.sub('\n {4}\]', ']', data)

    return data#json.dumps(formatted_fields)

# Set up the API credentials and endpoint URL
api_key = "77cb98527763da722c1fa622b65099c74a6742c57d2d4b1e3175c50a0873dec58bd7e0b4"
api_url = "https://lendconnectsandbox.api-us1.com/api/3/accountCustomFieldData" #"https://YOUR_ACCOUNT.api-us1.com/api/3/fields"
file = open("fields.json", "w")

# Send a GET request to the endpoint URL with the API key as a header
response = requests.get(api_url, headers={"Api-Token": api_key})
data = json.loads(response.text)

# Extract the necessary information
fields = data["fields"]

print(fields)

# Format the fields as JSON
formatted_fields = format_fields_as_json(fields)

formatted_fields = format_fields_as_json(fields)
file.write(formatted_fields)
file.close()

print(formatted_fields)