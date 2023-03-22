def removeCharacter(str, char_to_remove):
    return str.replace(char_to_remove.lower(), "").replace(char_to_remove.upper(), "").strip().capitalize()


alpha_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("\n\nThe Alphabet Fades Away\n")
input_string = "No more letter"

for char in alpha_str:
    print(f"{input_string} {char}")
    input_string = removeCharacter(input_string, char)
    if (input_string == ""):
        break

print("\n")