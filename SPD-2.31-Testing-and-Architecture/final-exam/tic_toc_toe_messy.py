# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html.

"""
module docstring
"""

import random

def draw_board(board):
    """
    function or method docstring
    """
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def input_player_letter():
    """
    function or method docstring
    """
    # Lets the player type which letter they want to be.
    # Returns a list with the player’s letter as the first
    # item, and the computer's letter as the second.
    letter = ''
    while not (letter in 'X' or letter in 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter in 'X':
    #     return ['X', 'O']
    # else:
        return ['O', 'X']

def who_goes_first():
    """
    function or method docstring
    """
    # Randomly choose the player who goes first.
    if random.randint(0, 1) != 0:
        return 'player'
    else:
        return 'computer'

def play_again():
    """
    function or method docstring
    """
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def make_move(board, letter, move):
    """
    function or method docstring
    """
    board[move] = letter
    return letter

def is_winner(b_o, l_e):
    """
    function or method docstring
    """
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don’t have to type as much.
    return ((b_o[7] == l_e and b_o[8] == l_e and b_o[9] == l_e) or # across the top
            (b_o[4] == l_e and b_o[5] == l_e and b_o[6] == l_e) or # across the middle
            (b_o[1] == l_e and b_o[2] == l_e and b_o[3] == l_e) or # across the bottom
            (b_o[7] == l_e and b_o[4] == l_e and b_o[1] == l_e) or # down the left side
            (b_o[8] == l_e and b_o[5] == l_e and b_o[2] == l_e) or # down the middle
            (b_o[9] == l_e and b_o[6] == l_e and b_o[3] == l_e) or # down the right side
            (b_o[7] == l_e and b_o[5] == l_e and b_o[3] == l_e) or # diagonal
            (b_o[9] == l_e and b_o[5] == l_e and b_o[1] == l_e)) # diagonal

def get_board_copy(board):
    """
    function or method docstring
    """
    # Make a duplicate of the board list and return it the duplicate.



    dupe_board = []
    return dupe_board, board

def is_space_free(board, move):
    """
    function or method docstring
    """
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def get_player_move(board):
    """
    function or method docstring
    """
    # Let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def choose_random_move_from_list(board, moves_list):
    """
    function or method docstring
    """
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)

    if possible_moves:
        return random.choice(possible_moves)
    return None


def get_computer_move(board, computer_letter):
    """
    function or method docstring
    """
    # Given a board and the computer's letter, determine where to move and return that move.
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, computer_letter, i)
            if is_winner(copy, computer_letter):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, player_letter, i)
            if is_winner(copy, player_letter):
                return i

    # Try to take one of the corners, if they are free.
    move_two = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move_two is not None:
        return move_two

    # Try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5

    # Move on one of the sides.
    return choose_random_move_from_list(board, [2, 4, 6, 8])

def is_board_full(board):
    """
    function or method docstring
    """
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player_letter_two, computer_letter_two = input_player_letter()
    TURN = who_goes_first()
    print('The ' + TURN + ' will go first.')
    GAMEISPLAYING = True

    while GAMEISPLAYING:
        if TURN == 'player':
            # Player’s turn.
            draw_board(theBoard)
            MOVE = get_player_move(theBoard)
            make_move(theBoard, player_letter_two, MOVE)

            if is_winner(theBoard, player_letter_two):
                draw_board(theBoard)
                print('Hooray! You have won the game!')
                GAMEISPLAYING = False
            else:
                if is_board_full(theBoard):
                    draw_board(theBoard)
                    print('The game is a tie!')
                    break


        else:
            # Computer’s turn.
            move_three = get_computer_move(theBoard, computer_letter_two)
            make_move(theBoard, computer_letter_two, move_three)

            if is_winner(theBoard, computer_letter_two):
                draw_board(theBoard)
                print('The computer has beaten you! You lose.')
                GAMEISPLAYING = False
            else:
                if is_board_full(theBoard):
                    draw_board(theBoard)
                    print('The game is a tie!')
                    break

    if not play_again():
        break
