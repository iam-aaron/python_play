input_limerick = """The limerick packs laughs astronomical
Into space that is quite economical
But the good ones I've seen
Very seldom are clean
And the clean ones so seldom are comical."""

processed_limerick = ""

for line in input_limerick.split("\n"):
    half_length = len(line) // 2
    first_half = line[:half_length] + "\n"
    second_half = "-"*half_length + line[half_length:] + "\n"

    processed_limerick += first_half + second_half


print(f"\nINPUT: \n{input_limerick}")

print(f"\n\nOUTPUT: \n{processed_limerick}")
