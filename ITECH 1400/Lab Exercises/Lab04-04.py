

input_str = input("Please enter a string: ")
reconstructed_str = ""

# START APPROACH 1
# for i in range(len(input_str)):
#     curr_char = input_str[i]

#     if (curr_char.isalpha()):
#         if i % 2 == 0:
#             reconstructed_str += curr_char.upper()
#         else:
#             reconstructed_str += curr_char.lower()
#     else:
#         reconstructed_str += curr_char

# END APPROACH 1


# START APPROACH 2
reconstructed_str = list(input_str)

for index, item in enumerate(reconstructed_str):
    if (item.isalpha()):
        if index % 2 == 0:
            reconstructed_str[index] = item.upper()
        else:
            reconstructed_str[index] = item.lower()

reconstructed_str = "".join(reconstructed_str)
# END APPROACH 1

print(reconstructed_str)
