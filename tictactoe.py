#Display Board Function
from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('-'+'-|-'+'-'+'-|--')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('-'+'-|-'+'-'+'-|--')
    print(board[1]+' | '+board[2]+' | '+board[3])

#Player Marker Input Function
def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player1: Chose X or O: ').upper()
    if marker == 'X':
          return ('X', 'O')
    else:
        return ('O', 'X')

#Placing marker into board position
def place_marker(board, marker, position):

    board[position] = marker

#Win Check for the game
def win_check(board, mark):

  #check all rows if they have same marker?
  return ((board[1] == mark and board[2] == mark and board[3]== mark)or
  (board[4] == mark and board[5] == mark and board[6]== mark)or
  (board[7] == mark and board[8] == mark and board[9]== mark)or
  #check all colomns if they have same marker?
  (board[1] == mark and board[4] == mark and board[7]== mark)or
  (board[2] == mark and board[5] == mark and board[8]== mark)or
  (board[3] == mark and board[6] == mark and board[9]== mark)or
  #check all diagonal if they have same marker?
  (board[1] == mark and board[5] == mark and board[9]== mark)or
  (board[3] == mark and board[5] == mark and board[7]== mark))

#Randomly decide which player goes first
import random
def choose_first():
  flip = random.randint(0,1)
  if flip == 1:
    return 'Player 1'
  else:
    return 'Player 2'

#Check for the space in the board
def space_check(board, position):

    return board[position] == ' '

#Check if the board is full
def full_board_check(board):

    for i in range(1,10):
      if space_check(board,i):
        return False

    return True

#asks for a player's next position (as a number 1-9)
def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
      position = int(input('Choose a position:(1-9) '))

    return position

#asks the player if they want to play again
def replay():

    choice = input('Play again? Enter Yes or No')

    return choice == 'Yes'

#Game Code
print('Welcome to Tic Tac Toe!')

#WHILE LOOP TO KEEP RUNNING THE GAME

while True:

  # PLAY THE GAME
  ## SET EVERYTHING UP 9BOARD, WHOS FIRST, CHOOSE MARKERS X,O
  the_board = [' ']*10
  player1_marker,player2_marker = player_input()

  turn = choose_first()
  print(turn + ' will go first')

  play_game = input('Ready to play? y or n? ')

  if play_game.lower()[0] == 'y':
    game_on = True
  else:
    game_on = False

  ## GAME PLAY

  while game_on:
    if turn == 'Player 1':
      ### PLAY ONE TURN
      #Show the board
      display_board(the_board)

      #choose a position
      position = player_choice(the_board)

      #place the marker on the position
      place_marker(the_board,player1_marker,position)

      #check if the won
      if win_check(the_board,player1_marker):
        display_board(the_board)
        print('PLAYER 1 HAS WON')
        game_on = False
      else:
      #or check if there is a tie
        if full_board_check(the_board):
          display_board(the_board)
          print('TIE GAME!')
          game_on = False
        else:
          #no tie and no win? Then next player's turn
          turn = 'Player 2'
    else:
      ### PLAY TWO TURN
      #Show the board
      display_board(the_board)

      #choose a position
      position = player_choice(the_board)

      #place the marker on the position
      place_marker(the_board,player2_marker,position)

      if win_check(the_board,player2_marker):
        display_board(the_board)
        print('PLAYER 2 HAS WON')
        game_on = False
      else:
      #or check if there is a tie
        if full_board_check(the_board):
          display_board(the_board)
          print('TIE GAME!')
          game_on = False
        else:
          #no tie and no win? Then next player's turn
          turn = 'Player 1'

  # BREAK OUT OF THE WHILE LOOP ON replay()
  if not replay():
    break

