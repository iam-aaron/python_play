# --------- TASK 1 START -----------
def collatzSequence(n):
    if n == 1: #if the number is 1 then f(n) = 1
        return [1] #returns a list of 1
    elif n%2 == 0: #if the number is even then f(n) = n/2
        return [n] + collatzSequence(n//2) #returns a list of the number and the collatz sequence of n/2
    else: #if the number is odd then f(n) = (3*n) + 1
        return [n] + collatzSequence((3*n) + 1) #returns a list of the number and the collatz sequence of (3*n) + 1
# --------- TASK 1 END -----------


def main(): #main function
    print("\n[TASK 01] COLLATZ SEQUENCE\n")

    input_num = int(input("\tEnter a postive integer: ")) #gets the input number
    print(f"\tThe Collatz Sequence of number {input_num} is {collatzSequence(input_num)}\n")


if __name__ == "__main__": #runs the main function
    main()