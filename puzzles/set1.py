#!/usr/bin/env python  

# Source: https://www.w3resource.com/python-exercises/puzzles/index.php

# EXER 1
# Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False
def isValidForExer1(arr):
    return arr.count(19) == 2 and arr.count(5) >= 3

# EXER 2
# Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
def isValidForExer2(arr):
    return len(arr) == 8 and arr.count(arr[4]) == 3

# EXER 3
# We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile.
def makeStonePileExer3(ph):
    return [ph+(iter*2) for iter in range(ph)]

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


#FOR EXER 1
#array_input = [19, 20, 15, 5, 3, 6, 7, 2]
#res = isValidForExer1(array_input)


#FOR EXER 2
#array_input = [11, 12, 14, 13, 14, 13, 15, 14]
#res = isValidForExer2(array_input)

#FOR EXER 3
#pileHeight = 10
#res = makeStonePileExer3(pileHeight)


#FOR EXER 4
#array_input = ['a', 'abb', 'sfs', 'oo', 'sfd', 'sfde']
#res = isValidForExer4(array_input)

#FOR EXER 5
array_input = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990]
res = isValidForExer5(array_input)

print(res)
