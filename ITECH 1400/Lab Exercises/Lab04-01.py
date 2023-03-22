
quote = "If you notice this notice you'll notice this notice is not worth noticing."
match = "notice"

location = 0
count = 0

while True:
    location = quote.find(match, location)
    if (location != -1):
        print(f"Found substring at: {location}")
        location += 1
        count += 1
    else:
        break

print(f"\nFound {count} occurrences of '{match}'\n")
