import os
import time

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1
Game = 0
Mark = 'X'

def DrawBoard():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print(" | | ")

def CheckPosition(x):
    if board[x] == ' ':
        return True
    else:
        return False

def CheckWin():
    global Game
    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        Game = 1
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        Game = 1
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        Game = 1
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        Game = 1
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        Game = 1
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        Game = 1
    elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
        Game = 1
    elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
        Game = 1
    elif board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and \
            board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and \
            board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
        Game = -1
    else:
        Game = 0

print("Tic-Tac-Toe Game Designed By Sourabh Somani")
print("Player 1 [X] --- Player 2 [O]\n")
print()
print()
print("Please Wait...")
time.sleep(3)

while Game == 0:
    os.system('cls')
    DrawBoard()

    if player % 2 != 0:
        print("Player 1's chance")
    else:
        print("Player 2's chance")
    
    Mark = input("Enter 'X' or 'O' to mark: ").upper()
    
    choice = int(input("Enter the position between [1-9] where you want to mark: "))
    if CheckPosition(choice):
        board[choice] = Mark
        player += 1
        CheckWin()

    os.system('cls')
    DrawBoard()

    if Game == -1:
        print("Game Draw")
    elif Game == 1:
        player -= 1
        if player % 2 != 0:
            print("Player 1 Won")
        else:
            print("Player 2 Won")
