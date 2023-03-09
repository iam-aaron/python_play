
import time
numberOfBottles = 99

for i in range(numberOfBottles, 0, -1):
    print("""
{0} bottles of beer on the wall, {0} bottles of beer.
Take one down, pass it around, {1} bottles of beer on the wall...""".format(i, i-1))
    time.sleep(0.5)
    if (i-1 == 0):
        print("""
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall...""")