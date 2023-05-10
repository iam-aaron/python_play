from Task01 import collatzSequence
from Task02 import maxLengths
from Task03 import maxValue

# --------- TASK 4 START -----------
def main(): #main function
    print("\n[TASK 04]!\n")

    input_num = int(input("\tEnter a postive integer: ")) #gets the input number

    maxLength_seq = maxLengths(input_num) #gets the longest sequence length and number
    maxValue_seq = maxValue(input_num) #gets the max sequence value and number

    print(collatzSequence(input_num))

    #prints the longest sequence length and number
    print(f"\nFor numbers <= {input_num}: ")
    print(f"{maxLength_seq[1]:>10} has the longest Collatz Sequence. The length is {maxLength_seq[0]}")
    print(f"{maxValue_seq[1]:>10} has the largest number in its Collatz Sequence. The number is {maxValue_seq[0]}\n")

# --------- TASK 4 END -----------


if __name__ == "__main__": #runs the main function
    main()