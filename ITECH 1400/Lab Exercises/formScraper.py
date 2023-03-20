import requests
from bs4 import BeautifulSoup

url = "https://www.geeksforgeeks.org/python-programming-language/" # replace with your URL

# send a GET request to the URL
response = requests.get(url)

# extract the HTML code from the response
html_code = response.text

# create a BeautifulSoup object with the HTML code
soup = BeautifulSoup(html_code, 'html.parser')

# find the form element in the HTML code
form = soup.find('form')

# extract the form action and method attributes
form_action = form.get('action')
form_method = form.get('method')

# extract the form input fields
form_inputs = {}
for input_tag in form.find_all('input'):
    input_name = input_tag.get('name')
    input_type = input_tag.get('type')
    input_value = input_tag.get('value')
    form_inputs[input_name] = {'type': input_type, 'value': input_value}

# print the form data
print("Form action:", form_action)
print("Form method:", form_method)
print("Form inputs:", form_inputs)
