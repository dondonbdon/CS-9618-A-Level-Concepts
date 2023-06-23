# Game of noughts and crosses / tic-tac-toe / x and o's

gridArr = [['' for j in range(3)] for i in range(3)]
occupied = []
player = True

def out_item(i, j):
    if gridArr[i][j] == 'X' or gridArr[i][j] == 'O':
        return '\b'
    else:
        return ''


def un_out():
    for i in range(50):
        print("\b")


def output_game():
    print(f'''
        0       1       2
     ________________________
    |	    |	    |	     |
0   |   {gridArr[0][0]}    {out_item(0, 0)}|   {gridArr[0][1]}    {out_item(0, 1)}|    {gridArr[0][2]}    {out_item(0, 2)}|
    |_______|_______|________|
    |	    |	    |	     |
1   |   {gridArr[1][0]}    {out_item(1, 0)}|   {gridArr[1][1]}    {out_item(1, 1)}|    {gridArr[1][2]}    {out_item(1, 2)}|
    |_______|_______|________|
    |	    |	    | 	     |
2   |   {gridArr[2][0]}    {out_item(2, 0)}|   {gridArr[2][1]}    {out_item(2, 1)}|    {gridArr[2][2]}    {out_item(2, 2)}|
    |_______|_______|________|
''')


def status():
    combinations = [[[0, 0], [0, 1], [0, 2]],
                    [[1, 0], [1, 1], [1, 2]],
                    [[2, 0], [2, 1], [2, 2]],
                    [[0, 0], [1, 0], [2, 0]],
                    [[0, 1], [1, 1], [2, 1]],
                    [[0, 2], [1, 2], [2, 2]],
                    [[0, 0], [1, 1], [2, 2]],
                    [[0, 2], [1, 1], [2, 0]]]

    for combination in combinations:
        value1 = gridArr[combination[0][0]][combination[0][1]]
        value2 = gridArr[combination[1][0]][combination[1][1]]
        value3 = gridArr[combination[2][0]][combination[2][1]]

        if value1 == 'X' and value2 == 'X' and value3 == 'X':
            return 0
        elif value1 == 'O' and value2 == 'O' and value3 == 'O':
            return 1

    return -1


def valid(st):
    combinations = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
    for s in combinations:
        if s == st.strip():
            return True
    else:
        return False


def parse(st):
    arr = []
    for i in list(st):
        arr.append(int(i))

    return arr


def add(grid_pos):
    gp = parse(grid_pos)
    occupied.append(gp)

    if player:
        gridArr[gp[0]][gp[1]] = 'X'
    else:
        gridArr[gp[0]][gp[1]] = 'O'


def get_row_size(i):
    size = 0
    for j in range(3):
        if gridArr[i][j] == 'X' or gridArr[i][j] == 'O':
            size += 1
    return size


def get_grid_size():
    size = 0
    for i in range(3):
        for j in range(3):
            if gridArr[i][j] == 'X' or gridArr[i][j] == 'O':
                size += 1

    return size


def get_player():
    if player:
        return 0

    return 1


def start_game():
    global player
    while get_grid_size() < 9 and status() == -1:
        st = input(f'Player{get_player()} - Enter your desired grid: ')
        while not valid(st):
            st = input(f'Player{get_player()} - Enter your desired grid: ')

        add(st)
        output_game()
        player = not player
    else:
        if status() == 0:
            print(f'Player0 won')
        elif status() == 1:
            print(f'Player1 won')
        else:
            print('Draw')


start_game()
