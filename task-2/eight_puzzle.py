import copy

def initial_state():
    return ((7, 2, 4, 5, 0, 6, 8, 3, 1), 1, 1)

def is_goal(s):
    return s[0] == (1, 2, 3, 4, 5, 6, 7, 8, 0)

def successors(s):
    _, r, c = s
    new_r, new_c = r-1, c
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r+1, c
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r, c-1
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r, c+1
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1

def is_valid(r, c):
    return 0 <= r <= 2 and 0 <= c <= 2

def move_blank(s, new_r, new_c):
    board, r, c = s
    new_board = list(board)
    new_board[r*3 + c] = new_board[new_r*3 + new_c]
    new_board[new_r*3 + new_c] = 0
    return (tuple(new_board), new_r, new_c)

def h1(s):
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    board, _, _ = s
    res = 0
    # The for loop counts the number of elements that is different from
    # the goal configuration.
    # We start from index 1 to 8 because the blank is excluded.
    for idx in range(1, 9):
        if goal[idx] != board[idx]:
            res += 1
    return res

def current_r(index):
    if index in [0,1,2] :
        return 0
    elif index in [3,4,5]:
        return 1
    else:
        return 2
     
def current_c(index):
    if index in [0,3,6]:
        return 0
    elif index in [1,4,7]:
        return 1
    else:
        return 2

def correct_r(value):
    correct_rows = {
        1: 0, 2: 0, 3: 0,
        4: 1, 5: 1, 6: 1,
        7: 2, 8: 2, 0: 2 
    }
    return correct_rows[value]
    
def correct_c(value):
    correct_cols = {
        1: 0, 2: 1, 3: 2,
        4: 0, 5: 1, 6: 2,
        7: 0, 8: 1, 0: 2 
    }
    return correct_cols[value]

def h3(s):
    # implement this function
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    board, _, _ = s
    res = 0
    wrongcolumn = 0
    wrongrow = 0
    for idx in range(0, 9):
        if goal[idx] != board[idx]:
            value = board[idx]
            curr_r = current_r(idx)
            curr_c = current_c(idx)
            corr_r = correct_r(value)
            corr_c = correct_c(value)
            if curr_c != corr_c:
                wrongcolumn += 1
            if curr_r != corr_r:
                wrongrow += 1
    res = wrongcolumn + wrongrow
    return res
