#!/usr/bin/env python  








# EXER 4
# Write a Python program to check the nth-1 string is a proper substring of the nth string in a given list of strings.
def isValidForExer4(arr):
    return (arr[len(arr)-2] in arr[len(arr)-1]) and (len(arr[len(arr)-2]) < len(arr[len(arr)-1]))

# EXER 5
# Write a Python program to test a list of one hundred integers between 0 and 999, which all differ by ten from one another. Return True otherwise False.
def isValidForExer5(arr):
    a = zip(arr, arr[1::])
    #print(list(y in range(1000) and y-x==10 for x,y in a))
    return  (all(list(y in range(1000) and y-x==10 for x,y in a)) and len(arr)==100)

# EXER 6
# Write a Python program to check a given list of integers where the sum of the first i integers is i.
def isValidForExer6(arr):

    print([sum(arr[:i]) == i for i in range(len(arr))])
    return len(arr) == sum(arr)

# EXER 7
# Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators. 
# help: https://pynative.com/python-regex-split/
def splitExer7(str):
    import re
    merged = re.split(r"([ ,]+)", str)
    return [merged[::2], merged[1::2]]

# EXER 9
# Write a Python program to find a list of integers containing exactly four distinct values, such that no integer repeats twice consecutively among the first sixteen entries
def isValidForExer9(arr):
    return all(arr[i] != arr[i+1] for i in range(len(arr)-1)) and len(set(arr)) == 4

# EXER 10
# Given a string consisting of whitespace and groups of matched parentheses, write a Python program to split it into groups of perfectly matched parentheses without any whitespace. 
def cleanUpSpaces(str):
    grouped_pair = []
    group = ""
    for prnthss in str.replace(" ", ""):
        group += prnthss
        if group.count("(") == group.count(")"):
            grouped_pair.append(group)
            group = ""
    return grouped_pair

# EXER 11
# Write a Python program to find the indexes of numbers in a given list below a given threshold. 
def findIndexes(thresh, arr):
    #return [i for i in range(len(arr)) if arr[i] < thresh]
    return [i for i,n in enumerate(arr) if arr[i] < thresh]

#-------------------------#
t = 10
input_arr = [0, 12, 4, 3, 49, 9, 1, 5, 3]
res = findIndexes(t, input_arr)

#FOR EXER 10
#str_input = "( ()) ((()()())) (()) ()"
#res = cleanUpSpaces(str_input)


#FOR EXER 9
#array_input = [1, 2, 3, 4, 4, 2, 3, 1, 1, 2, 3, 4, 1, 2, 3, 4]
#res = isValidForExer9(array_input)





#FOR EXER 3
#pileHeight = 10
#res = makeStonePileExer3(pileHeight)


#FOR EXER 4
#array_input = ['a', 'abb', 'sfs', 'oo', 'sfd', 'sfde']
#res = isValidForExer4(array_input)

#FOR EXER 5
#array_input = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990]
#res = isValidForExer5(array_input)

#FOR EXER 6
#array_input = [1,2,3,1,1]
#res = isValidForExer6(array_input)

#FOR EXER 7
#str_input = "The colors in my studyroom are blue, green, and yellow."
#res = splitExer7(str_input)

print(res)
