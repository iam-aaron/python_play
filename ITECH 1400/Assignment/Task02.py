from Task01 import collatzSequence

# --------- TASK 2 START -----------
def maxLengths(m):
    longest_seq_num = 0 #initializes the longest sequence number
    longest_seq_len = 0 #initializes the longest sequence length

    for i in range(m, 0, -1):  #loops through the numbers from input number to 1
        seq = collatzSequence(i) #gets the collatz sequence of the current number
        curr_seq_len = len(seq) #gets the length of the current sequence
        
        if (curr_seq_len > longest_seq_len): #change longest sequence length and number if the current sequence is longer than longest sequence
            longest_seq_len = curr_seq_len
            longest_seq_num = i

    return [longest_seq_len, longest_seq_num] #returns the longest sequence length and number
# --------- TASK 2 END -----------

def main(): #main function
    print("\n[TASK 02] COLLATZ SEQUENCE MAX LENGTHS\n")

    input_num = int(input("\tEnter a postive integer: ")) #gets the input number
    maxLength_seq = maxLengths(input_num) #gets the longest sequence length and number

    print(f"\nFor numbers <= {input_num}: ")
    print(f"{maxLength_seq[1]:>10} has the longest Collatz Sequence. The length is {maxLength_seq[0]} \n")

if __name__ == "__main__": #runs the main function
    main()