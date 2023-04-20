import random
import string

# Set password length
length = int(input("Enter the length of password: "))

# Define characters to be used
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

# Combine characters based on criteria
criteria = []
criteria.extend(list(lowercase))
criteria.extend(list(uppercase))
criteria.extend(list(digits))
criteria.extend(list(symbols))

# Remove characters that are hard to distinguish
for char in ['l', '1', 'I', 'O', '0']:
    criteria.remove(char)

# Generate password
password = ''.join(random.choices(criteria, k=length))

# Print password
print("Your password is: " + password)

# Write password to notes app
with open("passwords.txt", "a") as file:
    file.write(password + "\n")
