print("\n\nWELCOME TO CASE-INSENSITIVEWORD SEARCH COUNTER!")
match = input("\nPlease enter a word to count occurences of: ")

file = open("alice_in_wonderland.txt", "r")
line_count = 1
count = 0

# while True:
#     line = file.readline()
#     location = 0
#     if (line != ""):
#         while True:
#             location = line.lower().find(match.lower(), location)
#             if (location != -1):
#                 print(
#                     f"Found substring at line {line_count} at position {location}")
#                 location += 1
#                 count += 1
#             else:
#                 break
#     else:
#         break
#     line_count += 1


for line in file:
    location = 0
    while True:
        location = line.lower().find(match.lower(), location)
        if (location != -1):
            print(
                f"Found substring at line {line_count} at position {location}")
            location += 1
            count += 1
        else:
            break

    line_count += 1



print(f"\nThe word {match} appears {count} times in this book.")

file.close()
