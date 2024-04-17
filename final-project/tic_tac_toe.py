import os
import time

#My variant of this game will be "wild tic tac toe", this allows players to choose 
#whether they want to put an "x" or an "o" on each move


board = [' ']*10
player = 1
Game = 0

# Win Flags
Win = 1
Draw = -1
Running = 0

Game = Running

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
        Game = Win
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        Game = Win
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        Game = Win
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        Game = Win
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        Game = Win
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        Game = Win
    elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
        Game = Win
    elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
        Game = Win
    elif board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and \
            board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and \
            board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
        Game = Draw
    else:
        Game = Running


print("Wild Tic Tac Toe - Players can choose 'X' or 'O' on each move") #print statement so the player knows they can choose 'x' or 'o'
print("Player 1's mark: 'X'")
print("Player 2's mark: 'O'")
print("\nPlease Wait...")
time.sleep(3)

while Game == Running:
    os.system('cls')
    DrawBoard()

    if player % 2 != 0:
        print("Player 1's chance")
    else:
        print("Player 2's chance")

    mark = input("Enter your mark ('X' or 'O'): ").upper() #player must choose between x or o

    if mark not in ['X', 'O']: # I used an if statement to make sure the player types in x or o
        print("Invalid input. Please enter 'X' or 'O'")
        continue

    choice = int(input("Enter the position between [1-9] where you want to mark: "))
    
    if CheckPosition(choice):
        board[choice] = mark #The board is updated so that the players mark is either x or o, instead of a hardcoded mark based on the player
        player += 1
        CheckWin()

    os.system('cls')
    DrawBoard()

    if Game == Draw:
        print("Game Draw")
    elif Game == Win:
        player -= 1
        print(f"Player {player} Won")
