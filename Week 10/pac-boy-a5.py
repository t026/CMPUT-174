import random

BOARD_SIZE = 5
PAC_BOY = '👦'
MELON = '🍉'
GHOST = '👻'
EMPTY = '🔹'
NUMBER_OF_GHOSTS = 3
NUMBER_OF_MELONS = 5
def create_board():
    board = []
    for row_index in range(BOARD_SIZE):
        row = []
        for col_index in range(BOARD_SIZE):
            row.append(EMPTY)
        board.append(row)
    return board

def display_game_status(board, melons_eaten):
    print('GAME STATUS')
    for row_index in range(BOARD_SIZE):
        display_str =''
        for col_index in range(BOARD_SIZE):
            display_str = f'{display_str}{board[row_index][col_index]:^5}'
        print(display_str)
    print(f'MELONS EATEN SO FAR :{melons_eaten}')

def place_items(board:list, p_loc:list,  items:list):
    row = p_loc[0]
    col = p_loc[1]
    board[row][col] = PAC_BOY
    for item in items:
        placed = False
        while not placed:
            row = random.randint(0,BOARD_SIZE -1)
            col = random.randint(0, BOARD_SIZE -1)
            if board[row][col] == EMPTY:
                board[row][col] = item
                placed = True

def update_location(move, p_loc)->bool:
    update = False
    row = p_loc[0]
    col = p_loc[1]
    if move == 'N':
        if row - 1 >=0:
            row = row - 1
            update = True
    elif move == 'S':
        if row + 1 <= BOARD_SIZE - 1:
            row = row + 1
            update = True
            
    elif move == 'W':
        if col - 1 >=0:
            col = col - 1
            update = True
    elif move == 'E':
        if col + 1 <= BOARD_SIZE - 1:
            col = col + 1
            update = True
    if update :
        p_loc[0] = row
        p_loc[1] = col
    else:
        print('Invalid Move')
    return update
        
def update_board(board, new_location, old_location):
    old_row = old_location[0]
    old_col = old_location[1]
    board[old_row][old_col] = EMPTY
    new_row = new_location[0]
    new_col = new_location[1]
    board[new_row][new_col] = PAC_BOY

def check_content(board,p_loc,melons_eaten):
    continue_game = True
    row = p_loc[0]
    col = p_loc[1]
    if board[row][col] == MELON:
        melons_eaten = melons_eaten + 1
        if melons_eaten == NUMBER_OF_MELONS:
            continue_game = False
    elif board[row][col] == GHOST:
        continue_game = False
    return continue_game,melons_eaten # returning a tuple

def display_outcome(melons_eaten):
    if melons_eaten == NUMBER_OF_MELONS:
        print('You win')
    else:
        print('A ghost scared you!')
def main():
    # 1. Create the board
    board = create_board()
    # 2. Display the board
    melons_eaten = 0
    display_game_status(board, melons_eaten)
    # 3. Place items on the board
    p_loc = [0,0]
    items = [GHOST] * NUMBER_OF_GHOSTS + [MELON] * NUMBER_OF_MELONS
    place_items(board, p_loc, items)
    display_game_status(board, melons_eaten)
    # 4. We will start the game and we will ask the user to enter the move
    continue_game = True
    while continue_game:
        move = input('Enter move >').upper()
        # 5. Update location of PAC BOY
        p_loc_copy = p_loc[:] #cloning
        update = update_location(move, p_loc)
        if update:
            # 6. CHECK CONTENT of the cell
            continue_game,melons_eaten = check_content(board,p_loc,melons_eaten)
            # 7. UPDATE THE BOARD
            update_board(board,p_loc,p_loc_copy)
            display_game_status(board, melons_eaten)
    display_outcome(melons_eaten)
            
if __name__ == '__main__':
    main()