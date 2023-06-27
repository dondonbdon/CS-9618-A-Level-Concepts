# Game of noughts and crosses / tic-tac-toe / x and o's

grid = [['' for j in range(3)] for i in range(3)]
occupied = []
player = True


def output_visual_backspacer(i, j):
    if grid[i][j] == 'X' or grid[i][j] == 'O':
        return '\b'
    else:
        return ''


def output_visual():
    print(f'''
        0       1       2
     ________________________
    |	    |	    |	     |
0   |   {grid[0][0]}    {output_visual_backspacer(0, 0)}|   {grid[0][1]}    {output_visual_backspacer(0, 1)}|    {grid[0][2]}    {output_visual_backspacer(0, 2)}|
    |_______|_______|________|
    |	    |	    |	     |
1   |   {grid[1][0]}    {output_visual_backspacer(1, 0)}|   {grid[1][1]}    {output_visual_backspacer(1, 1)}|    {grid[1][2]}    {output_visual_backspacer(1, 2)}|
    |_______|_______|________|
    |	    |	    | 	     |
2   |   {grid[2][0]}    {output_visual_backspacer(2, 0)}|   {grid[2][1]}    {output_visual_backspacer(2, 1)}|    {grid[2][2]}    {output_visual_backspacer(2, 2)}|
    |_______|_______|________|
''')


def gane_status():
    combinations = [[[0, 0], [0, 1], [0, 2]],
                    [[1, 0], [1, 1], [1, 2]],
                    [[2, 0], [2, 1], [2, 2]],
                    [[0, 0], [1, 0], [2, 0]],
                    [[0, 1], [1, 1], [2, 1]],
                    [[0, 2], [1, 2], [2, 2]],
                    [[0, 0], [1, 1], [2, 2]],
                    [[0, 2], [1, 1], [2, 0]]]

    for combination in combinations:
        value1 = grid[combination[0][0]][combination[0][1]]
        value2 = grid[combination[1][0]][combination[1][1]]
        value3 = grid[combination[2][0]][combination[2][1]]

        if value1 == 'X' and value2 == 'X' and value3 == 'X':
            return 0
        elif value1 == 'O' and value2 == 'O' and value3 == 'O':
            return 1

    return -1


def validate_input(res):
    for i in occupied:
        if res == i:
            return False
    
    combinations = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
    for s in combinations:
        if s == res.strip():
            return True
    else:
        return False


def parse(res):
    arr = []
    for i in list(res):
        arr.append(int(i))
    arr.reverse()
    return arr


def on_play(grid_pos):
    gp = parse(grid_pos)
    
    occupied.append(grid_pos)
    if player:
        grid[gp[0]][gp[1]] = 'X'
    else:
        grid[gp[0]][gp[1]] = 'O'


def get_grid_size():
    size = 0
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'X' or grid[i][j] == 'O':
                size += 1

    return size


def get_current_player():
    if player:
        return 0

    return 1

def polarise( val):
    return not val

def start_game():
    global player
    while get_grid_size() < 9 and gane_status() == -1:
        res = input(f'Player {get_current_player()}: ')
        while not validate_input(res):
            res = input(
                f'Player {get_current_player()}: ')

        on_play(res)
        output_visual()
        player = polarise(player)
    else:
        if gane_status() == 0:
            print('Player 0 won')
        elif gane_status() == 1:
            print('Player 1 won')
        else:
            print('Draw')


start_game()
