import random
import time
import os.path
import json
random.seed()


def draw_board(board):
    # drawing the board
    """
    Draw the current state of the Tic-Tac-Toe board
    :param board: The current state of the board
    """
    for row in board:
        print("|".join(row))
        print("------")

def welcome(board):
    # prints the welcome message
    # display the board by calling draw_board(board)
    """
    Display the welcome message and draw the board
    :param board: The current state of the board
    """
    print('Welcome to the "Unbeatable Noughts and Crosses" game.')
    print("The board layout is shown  below:")
    draw_board(board)
    print("Enter the number corresponding to the square you want.")



def initialise_board(board):
    # develop code to set all elements of the board to one space ' '
    """
    Initialise all cells in the board to empty spaces ' '
    :param board: The current state of the board
    :return: The initialised board
    """
    for row in range(3):
        for col in range(3):
            board[row][col] =" "
    return board
    

def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    # and return row and col
    """
    Get the player's move
    :param board: The current state of the board
    :return: The row and column of the player's move
    """
    while True:
        move = int(input("Enter a number (1-9) for your move: "))
        move=move-1
        try:
            
            if 0 <= move <= 9:
                row, col = move // 3, move % 3
                if board[row][col] == " ":
                    board[row][col] = "X"
                    return row, col
                else:
                    print("cell is already occupied. Please chose another.")
            else:
                print("Invalid move. Please Choose between 1-9")
        except ValueError:
            print("Invalid move. Please Enter a Valid Move")
    
   
        

def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    # and return row and col
    """
    Choose a random move for the computer
    :param board: The current state of the board
    :return: The row and column of the computer's move
    """
    # Develop code to let the computer choose a cell to put a nought in
    # and return row and col

    # Check rows for player's X
    for i in range(3):
        count = 0
        for j in range(3):
            if board[i][j] == "X":
                count += 1
        if count == 2:
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    return i, j

    # Check columns for player's X
    for j in range(3):
        count = 0
        for i in range(3):
            if board[i][j] == "X":
                count += 1
        if count == 2:
            for i in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    return i, j

    # Check top-left to bottom-right diagonal for player's X
    count = 0
    for i in range(3):
        if board[i][i] == "X":
            count += 1
    if count == 2:
        for i in range(3):
            if board[i][i] == " ":
                board[i][i] = "O"
                return i, i

    # Check top-right to bottom-left diagonal for player's X
    count = 0
    for i in range(3):
        if board[i][2 - i] == "X":
            count += 1
    if count == 2:
        for i in range(3):
            if board[i][2 - i] == " ":
                board[i][2 - i] = "O"
                return i, 2 - i

    # If no winning move for player X is found, choose a random cell
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = "O"
            return row, col



def check_for_win(board, mark):
    
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    """
    Check if a player has won the game
    :param board: The current state of the board
    :param mark: The player's mark, either 'X' or 'O'
    :return: True if the player has won, False otherwise
    """
    
    if board[0][0] == mark and board[0][1] == mark and board[0][2] == mark:
        return True
    elif board[1][0] == mark and board[1][1] == mark and board[1][2] == mark:
        return True
    elif board[2][0] == mark and board[2][1] == mark and board[2][2] == mark:
        return True
    elif board[0][0] == mark and board[1][0] == mark and board[2][0] == mark:
        return True
    elif board[0][1] == mark and board[1][1] == mark and board[2][1] == mark:
        return True
    elif board[0][2] == mark and board[1][2] == mark and board[2][2] == mark:
        return True
    elif board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True
    elif board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    else:
        return False
    

def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    """
    cheks for draw.
    :param board: The current state of the board
    :return: True if the game is draw, False otherwise
    """

    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return False
    return True

def play_game(board):
    """
    This function plays a game of tic-tac-toe between the player and the computer.
    :param board: The current state of the board
    Returns:1 if the player has won, -1 if the comouter has won and 0 if the game is draw
    """
    initialise_board(board)
    draw_board(board)

    while True:
        row, col = get_player_move(board)
        board[row][col] = "X"
        draw_board(board)
        if check_for_win(board, "X"):
            print("Congratulations! You won.")
            return 1
        elif check_for_draw(board):
            print("It's a draw.")
            return 0
        print("It's computer's turn.")
        time.sleep(0.7)
        row, col = choose_computer_move(board)
        board[row][col] = "O"
        draw_board(board)
        if check_for_win(board, "O"):
            print("Computer wins. Better luck next time.")
            return -1
        elif check_for_draw(board):
            print("It's a draw.")
            return 0
        

           




def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    '''
    the function gets user input for choice and retruns one of the following:
    1 - To play the game
    2 - To save score in the file 'leaderboard.txt'
    3 - To load and display scores from the file 'leaderboard.txt'
    q - To end the program
    
    '''
    choice=input("""What would you like to do?
1 - Play the game
2 - Save score in file 
3 - Load and display the scores from the 'leaderboard.txt'
q - End the program
choise:""")
    if choice in ["1", "2", "3", "q"]:
        return choice.lower()
    else:
        print("Input valid choice!")
        return menu()

def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    """Loads the leaderboard scores from the file 'leaderboard.txt'
    Returns:
    leaders (dict): A dictionary with the player names as keys and the scores as values"""
    if os.path.exists("leaderboard.txt"):
        with open("leaderboard.txt","r") as file:
            try:
                leaders = json.load(file)
                return leaders
            except json.JSONDecodeError:
                print("unable to load data.")
                return {}
    else:
        return {}

                
            
                                
def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    """
    the function asks user for their name and save their current score in leaderboard.txt
    :param score:gets the total_score from the main file
    """
    name = input("Enter your name: ")
    leaderboard = {}
    if os.path.exists("leaderboard.txt"):
        with open("leaderboard.txt", "r") as file:
            leaderboard = json.load(file)
    leaderboard[name] = score
    with open("leaderboard.txt", "w") as file:
        json.dump(leaderboard, file)


  


def display_leaderboard(leaders):
    """
    the function print the dictionary with the player names as keys and the scores as values in assending order of the score
    :param leaders: A dictionary with the player names as keys and the scores as values
     """

    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    if len(leaders)==0:
        print("No Leaderboard data to display")
    else:
        sorted_leaders = sorted(leaders.items(), key=lambda x: x[1], reverse=True)
        print("{:<10}{:<10}".format("Name", "Score"))
    for leader in sorted_leaders:
        print("{:<10}{:<10}".format(leader[0], leader[1]))
        


    

