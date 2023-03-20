#!/usr/bin/env python 

# Source:

# EXER 1
# EASY Capital Indexes
# Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.
def capital_indexes(str):
    return [i for i in range(len(str)) if str[i].isupper()]

# EXER 2
# EASY Middle Letter
# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
def mid(str):
    return str[int(len(str)/2)] if len(str)%2 == 1 else ""

# EXER 3
# EASY Online Status
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline".
def online_count(stats):
    return len([usr for usr, stat in stats.items() if stat == "online"])

# EXER 4
# EASY 
# Define a function, random_number, that takes no parameters. The function must generate a random integer between 1 and 100, both inclusive, and return it.
def random_number():
    import random
    return random.randrange(1,100)

# EXER 5
# EASY Type Check
# Write a function named only_ints that takes an array. Your function should return True if all parameters are integers, and False otherwise.
def only_ints(arr):
    #return all([isinstance(i, int) and not isinstance(i, bool) for i in arr])
    return all([type(i) == int for i in arr])

# EXER 6
# EASY Double letters in a row
# Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.
def double_letters(str):
    return any([x == y for x,y in zip(str, str[1::])])

# START EXER 7
# EASY Add/Remove Dots in between characters
def add_dots(str):
    return ".".join(str)

def remove_dots(str):
    return str.replace(".", "")
# END EXER 7

# EXER 8
# EASY 
# Define a function named count that takes a single parameter. The parameter is a string. The string will contain a single word divided into syllables by hyphens
def count(str):
    return len(str.split("-"))

# EXER 9
# EASY Anagram
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

# EXER 9
# EASY Flatten list
def flatten(listoflists):
    return [item for sublist in listoflists for item in sublist]

# EXER 10
# EASY min/max
def largest_difference(arr):
    return max(arr)-min(arr)

# EXER 11
# EASY Divisible by 3
def div_3(num):
    return num % 3 == 0

# EXER 12
# TicTacToe getrowcol
def get_row_col(move):
    grid = {
        "A1": (0, 0),
        "A2": (1, 0),
        "A3": (2, 0),
        "B1": (0, 1),
        "B2": (1, 1),
        "B3": (2, 1),
        "C1": (0, 2),
        "C2": (1, 2),
        "C3": (2, 2),
    }
    return grid.get(move)

# EXER 13
# EASY Palindrome
def palindrome(word):
    return word == word[::-1]

# EXER 14
# EASY Up and Down
# Define a function named up_down that takes a single number as its parameter. Your function return a tuple containing two numbers; the first should be one lower than the parameter, and the second should be one higher.
def up_down(n):
    return (n-1, n+1)

# EXER 15
# EASY Consecutive Zeros
def consecutive_zeros(bin):
    return len(max(bin.split("1")))

# EXER 16
# EASY All equal
# Define a function named all_equal that takes a list and checks whether all elements in the list are the same.
def all_equal(arr):
    return all([arr[0] == i for i in arr])

# EXER 17
# EASY Boolean and
# Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.
def triple_and(param1, param2, param3):
    return all([param1, param2, param3])

# EXER 18
# EASY Writing short code
# Define a function named convert that takes a list of numbers as its only parameter and returns a list of each number converted to a string.
def convert(arr):
    #return [str(i) for i in arr]
    return list(map(str,arr))

# EXER 19
# EASY Custom Zip function
def zap(arr1, arr2):
    return list(map(lambda x,y: (x, y), arr1, arr2))

# EXER 20
# List XOR
# Your function must return whether n is exclusively in list1 or list2
def list_xor(n, arr1, arr2):
    return (n in arr1) ^ (n in arr2)

# EXER 21
# EASY Counting dynamic function parameters
def param_count(*params):
    return len(params)

# EXER 22
def format_number(n_str):
    #n_str_rev = (str(n_str))[::-1]
    #return ",".join([n_str_rev[i:i+3] for i in range(0,len(n_str_rev),3)])[::-1]
    return "{:,}".format(n_str)

def validate(code):
    if "def" not in code:
        return "missing def"
    if ":" not in code:
        return "missing :"
    if "(" not in code or ")" not in code:
        return "missing paren"
    if "(" + ")" in code:
        return "missing param"
    if "    " not in code:
        return "missing indent"
    if "validate" not in code:
        return "wrong name"
    if "return" not in code:
        return "missing return"
    return True

# Param for EXER 3
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

print(format_number(1000000))
