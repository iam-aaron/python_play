import time

# --------- TASK 1 START -----------
def collatzSequence2(n):
    sequence = [n]
    while (n!=1):
        n = int(n/2 if n%2 == 0 else (3*n) + 1)
        sequence.append(n)
    return sequence


def collatzSequence(n):
    if n == 1:
        return [1]
    elif n%2 == 0:
        return [n] + collatzSequence2(n/2)
    else:
        return [n] + collatzSequence2((3*n) + 1)
    
# --------- TASK 1 END -----------

# --------- TASK 2 START -----------
def maxLengths(m):
    longest_seq_num = 0
    longest_seq_len = 0

    for i in range(m, 0, -1): 
        seq = collatzSequence(i)
        curr_seq_len = len(seq)
        # print(f"{i:>3} length: {curr_seq_len:>3} sequence: {max(seq)}")
        if (curr_seq_len > longest_seq_len):
            longest_seq_len = curr_seq_len
            longest_seq_num = i

    return [longest_seq_len, longest_seq_num]


# --------- TASK 2 END -----------


# --------- TASK 3 START -----------
def maxValue(m):
    max_seq_num = 0
    max_seq_val = 0

    for i in range(1, m+1): 
        seq = collatzSequence(i)
        curr_seq_max = max(seq)
        # print(f"{i:>3} length: {curr_seq_max:>3} sequence: {max(seq)}")
        if (curr_seq_max > max_seq_val):
            max_seq_val = curr_seq_max
            max_seq_num = i

    return [max_seq_val, max_seq_num]


# --------- TASK 3 END -----------
        

# --------- TASK 4 START -----------

def main():
    print("\nWELCOME TO COLLATZ SEQUENCE GENERATOR BY AARON MEDINA!\n")

    input_num = int(input("\tEnter a postive integer: "))

    print(collatzSequence(input_num))

    start_time = time.time()
    maxLength_seq = maxLengths(input_num)
    maxValue_seq = maxValue(input_num)
    end_time = time.time()

    print(f"\nFor numbers <= {input_num}: ")
    print(f"{maxLength_seq[1]:>10} has the longest Collatz Sequence. The length is {maxLength_seq[0]}")
    print(f"{maxValue_seq[1]:>10} has the largest number in its Collatz Sequence. The number is {maxValue_seq[0]}\n")

    print(f"Your running time is {end_time-start_time}")

# --------- TASK 4 END -----------



if __name__ == "__main__":
    main()