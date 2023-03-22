def removeCharacter(str, char_to_remove):
    return str.replace(char_to_remove.lower(), "").replace(char_to_remove.upper(), "").strip()

alpha_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("\n\nThe Alphabet Fades Away\n")
input_string = "The quick brown fox jumps over the lazy dog"
input_string_len = len(input_string)

for char in alpha_str:
    print(f"{input_string:^{input_string_len}}") #{char:<{input_string_len}}")
    input_string = f"{removeCharacter(input_string, char)}"
    if (input_string == ""):
        break

print("\n")