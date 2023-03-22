def get_primes_in_range(start, end):
    prime_list = []

    for num in range(start, end + 1):
        if num > 1:
            found_divisor = False
            for i in range(2, int(num/2)+1):
                if (num % i == 0):
                    found_divisor = True
                    break

            if (found_divisor == False):
                prime_list.append(num)

    return prime_list


start_value = int(input("Enter the prime range starting value: "))
end_value = int(input("Enter the prime range ending value: "))
filename = input("Filename to write the primes to: ")

prime_list = get_primes_in_range(start_value, end_value)

file = open(filename, "w")

for value in prime_list:
    strValue=str(value)
    file.write(strValue + "\n")

file.close()
