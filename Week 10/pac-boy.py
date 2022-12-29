import random
from time import sleep
from playsound import playsound

BOARD_SIZE = 5
PAC_BOY = '👦'
MELON = '🍉'
GHOST = '👻'
EMPTY = '🔹'
NUMBER_OF_GHOSTS = 3
NUMBER_OF_MELONS = 5

def create_board():
    board =  [[EMPTY for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
    board[0][0] = PAC_BOY
    for i in range(NUMBER_OF_GHOSTS):
        while True:
            x = random.randint(0, 4)
            y = random.randint(0, 4)
            if board[x][y] == EMPTY:
                board[x][y] = GHOST
                break
    for i in range(NUMBER_OF_MELONS):
        while True:
            x = random.randint(0, 4)
            y = random.randint(0, 4)
            if board[x][y] == EMPTY:
                board[x][y] = MELON
                break      
    return board  

def display_game_status(board, melons_eaten):
    for i in range(BOARD_SIZE):
        row = ''
        for j in range(BOARD_SIZE):
            row += f"{board[i][j]:^5}"
        print(row)
    print(f"Melons eaten so far: {melons_eaten}\n")
        
def move_pac_boy(board, pac_boy_location, new_location):
    board[pac_boy_location[0]][pac_boy_location[1]] = EMPTY
    if board[new_location[0]][new_location[1]] == MELON:
        num = 1
        flag = True
    elif board[new_location[0]][new_location[1]] == GHOST:
        num = 0
        flag = False
    else:
        num = 0
        flag = True
    board[new_location[0]][new_location[1]] = PAC_BOY
    return new_location, flag, num

def user_turn(board, pac_boy_location, melons_eaten):
    while True:
        movement = input("Enter the direction you want to move in(w,a,s,d):").lower()
        if movement in ['w', 'a', 's', 'd']:
            if movement == 'n' and pac_boy_location[0] == 0 or movement == 's' and pac_boy_location[0] == 4 or movement == 'e' and pac_boy_location[1] == 4 or movement == 'w' and pac_boy_location[1] == 0:
                print("Move Invalid")
                sleep(0.5)
                display_game_status(board, melons_eaten)
            else:
                if movement == 'w':
                    new_location, flag, num = move_pac_boy(board, pac_boy_location, [pac_boy_location[0]-1, pac_boy_location[1]])
                elif movement == 's':
                    new_location, flag, num = move_pac_boy(board, pac_boy_location, [pac_boy_location[0]+1, pac_boy_location[1]])
                elif movement == 'd':
                    new_location, flag, num = move_pac_boy(board, pac_boy_location, [pac_boy_location[0], pac_boy_location[1]+1])
                elif movement == 'a':
                    new_location, flag, num = move_pac_boy(board, pac_boy_location, [pac_boy_location[0], pac_boy_location[1]-1])
                break
        else:
            print("Move invalid")
            sleep(0.5)
            display_game_status(board, melons_eaten)
    return flag, num, new_location

def main():
    board = create_board()
    melons_eaten = 0
    display_game_status(board, melons_eaten)
    pac_boy_location = [0,0]
    flag = True
    while flag:
        flag, num, pac_boy_location = user_turn(board, pac_boy_location, melons_eaten)
        melons_eaten += num
        display_game_status(board, melons_eaten)
        if melons_eaten == NUMBER_OF_MELONS:
            print("You ate all the melons and won!:)")
            playsound('win.mp3')
            break
    if not flag:
        print("You hit a ghost and lost!:(")
        playsound('lose.mp3')

if __name__ == "__main__":
    main()