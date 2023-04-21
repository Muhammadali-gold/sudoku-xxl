import random
import os


boards=[]


class GameManager:
  def __init__(self):
    pass


def print_instructions():
  print('Instructions:')
  print('1. Input new sudoku.')
  print('2. Solve random sudoku.')
  print('3. Exit.')


def is_valid(move):
  return 1

def start_game():
  global boards
  if len(boards)==0:
    print('Sudoku not found')
    return

  random.shuffle(boards)
  board_selected = boards[0]

  while 1:
    print_board(board_selected)
    move = input('Input move: ')
    if not is_valid(move):
      print('Move is not valid')
      break
      
    row,col,digit = move.split()
    board_selected[int(row)-1][int(col)-1] = digit
    os.system('clear')


def print_board(board):
  print('\n'.join([str(' '.join(b)) for b in board]))

  

def input_board():
  global boards
  s=input('Please input initial board: ')
  board = [list(b) for b in s.split('/')]
  boards.append(board)
  print('Sudoku saved!')
  
def main():
  while 1:
    print_instructions()
    cmd = input()
    if cmd == '3':
      print('Program exited successfully.')
      break
    if cmd == '2':
      print('Start game')
      start_game()
    if cmd == '1':
      input_board()


if __name__ == '__main__':
  main()
  # input_board()