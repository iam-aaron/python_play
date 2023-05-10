from Task01 import collatzSequence

# --------- TASK 3 START -----------
def maxValue(m):
    max_seq_num = 0 #initializes the max sequence number
    max_seq_val = 0 #initializes the max sequence value

    for i in range(1, m+1): #loops through the numbers from 1 to input number
        seq = collatzSequence(i) #gets the collatz sequence of the current number
        curr_seq_max = max(seq) #gets the max value of the current sequence
        
        if (curr_seq_max > max_seq_val): #change max sequence value and number if the current sequence is greater than max sequence number
            max_seq_val = curr_seq_max
            max_seq_num = i

    return [max_seq_val, max_seq_num] #returns the max sequence value and number
# --------- TASK 3 END -----------

def main(): #main function
    print("\n[TASK 03] COLLATZ SEQUENCE MAX VALUE\n")

    input_num = int(input("\tEnter a postive integer: ")) #gets the input number
    maxValue_seq = maxValue(input_num) #gets the max sequence value and number

    print(f"\nFor numbers <= {input_num}: ")
    print(f"{maxValue_seq[1]:>10} has the largest number in its Collatz Sequence. The number is {maxValue_seq[0]}\n")

if __name__ == "__main__": #runs the main function
    main()