

input_str = input("Please enter a string: ")
reconstructed_str = ""

for i in range(len(input_str)):
    curr_char = input_str[i]

    if (curr_char.isalpha()):
        if i % 2 == 0:
            reconstructed_str += curr_char.upper()
        else:
            reconstructed_str += curr_char.lower()
    else:
        reconstructed_str += curr_char

print(reconstructed_str)
