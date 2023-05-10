from gol import GameOfLife # importing GameOfLife class from gol.py
from gol_patterns import pulsar_pattern, glider_pattern, toad_pattern, corners_block_pattern # importing patterns from gol_patterns.py

def main():
    # Create a GameOfLife object
    board_size = 20 # 20 is the size of the board
    glt = GameOfLife(board_size) # create GameOfLife object
    valid_patterns = ["1", "2", "3", "4", "0"] # create list for pattern selection
    board_counter = 0 # counter for printed boards

    # print welcome message
    print(f"\n{'*' * 50}")
    print("Welcome to Aaron's Game of Life Console App".center(50))
    print(f"{'*' * 50}\n")

    while True: # loop until valid pattern is selected
        selected_pattern = input('''Available options
[1] Pulsar Pattern
[2] Glider Pattern
[3] Toad Pattern
[4] Corners Block Pattern
[0] QUIT GAME :(

    Select an option: ''')
        
        # this if/else is for checkick if selected pattern is valid, if not, loop again
        if selected_pattern in valid_patterns: 
            break # break loop if valid pattern is selected
        else:
            print("\n\nERROR! Invalid option, please select a valid pattern.\n")

    # assigning selected pattern to game board or exit
    if selected_pattern == "1":
        glt.board = pulsar_pattern
    elif selected_pattern == "2":
        glt.board = glider_pattern
    elif selected_pattern == "3":
        glt.board = toad_pattern
    elif selected_pattern == "4":
        glt.board = corners_block_pattern
    else:
        print("\n\nGoodbye!\n")
        exit()

    # loop to print next pattern or exit
    while True:
        print(f"\n\nBOARD #{board_counter}")
        glt.printBoard()
        glt.nextPattern()
        continue_game = input("To print the next pattern, enter Y or y, To end the game, press any other key: ") # prompt user to continue or exit game
        board_counter += 1 # increment board counter

        if continue_game.upper() != "Y": # if Y/y continue game, else exit
            print("\n\nThank you for playing, goodbye!\n")
            break

# main function
if __name__ == "__main__": # if this file is run directly, run main()
    main()