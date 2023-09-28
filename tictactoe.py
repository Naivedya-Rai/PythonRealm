#function to create the outline of the display board
def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])

#function to assign the markers to the players
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1 pick between X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
#function to ASSIGN the marker at the desired position
def place_marker(board, marker, position):
    board[position] = marker
    
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == board[9] == mark) or # first row
    (board[4] == board[5] == board[6] == mark) or # second row
    (board[1] == board[2] == board[3] == mark) or # third row
    (board[7] == board[4] == board[1] == mark) or # first column
    (board[8] == board[5] == board[2] == mark) or # second column
    (board[9] == board[6] == board[3] == mark) or # third column
    (board[7] == board[5] == board[3] == mark) or # first diagonal
    (board[9] == board[5] == board[1] == mark)) # second diagonal


import random

#function to decide which player goes first

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    
#function to check if a position is empty to assign the marker
def space_check(board, position):
    
    return board[position] == ' '

#function to check if the board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#function to pick players next marker position
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your position: (1-9) '))
    
        
    return position

#function to ask the players if they want to play again
def play_again():
 
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


#main code
print('Welcome to the Tic Tac Toe Game!')


#setting up the game
while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No :')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            
            display_board(theBoard)
            print('\n')
            print("player 1's turn")
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('PLAYER 1 WINS!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('its a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            print('\n')
            print("player 2's turn")
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has secured the dub!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('its a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not play_again():
        break