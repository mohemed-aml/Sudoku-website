#row array definition
row = [[ False, 9, [c for c in range(9)] ] for r in range(9)]

#column array definition
col = [[ False, 9, [c for c in range(9)] ] for r in range(9)]

#box array definition
box = [[ False, 9, [c for c in range(9)] ] for r in range(9)]

#set value function
def enter_val(ro, co, val):

    if (ro < 3 ):
        if (co < 3):
            bo = 1
        elif (co > 5):
            bo = 3
        else:
            bo = 2
    elif ( ro > 5):
           if (co < 3):
               bo = 7
           elif (co > 5):
               bo = 9
           else:
               bo = 8
    else :
        if (co < 3):
            bo = 4
        elif (co > 5):
            bo = 6
        else:
            bo = 5
    lst[row][col][1] = val
    lst[row][col][0] = True

    row[ro][1] -= 1
    row[ro][2].remove(val)
    print row[ro][2]

    col[co][1] -= 1
    col[co][2].remove(val)
    print col[co][2]

    box[bo][1] -= 1
    box[bo][2].remove(val)
    print box[bo][2]




# trial

# function to return the range for row and column of a box position
def get_box_range(bo):

    if (bo = 0):
        return ([ [0, 1, 2]], [0, 1, 2] ])
    elif (bo = 1):
        return ([ [0, 1, 2]], [3, 4, 5] ])
    elif (bo = 2):
        return ([ [0, 1, 2]], [6, 7, 8] ])
    elif (bo = 3):
        return ([ [3, 4, 5]], [0, 1, 2] ])
    elif (bo = 4):
        return ([ [3, 4, 5]], [3, 4, 5] ])
    elif (bo = 5):
        return ([ [3, 4, 5]], [6, 7, 8] ])
    elif (bo = 6):
        return ([ [6, 7, 8]], [0, 1, 2] ])
    elif (bo = 7):
        return ([ [6, 7, 8]], [3, 4, 5] ])
    else:
        return ([ [6, 7, 8]], [6, 7, 8] ])

# function to check the other cells in rows, columns and box which conatin a particular cell
def check_related_cells(ro, co, bo):

    for r in range(9):
        if(lst[r][co][1] == '-'):
            b = val_box(r, co)
            x = check_cell(r, co, b)

    for c in range(9):
        if( lst[ro][c][1] == '-'):
            b = val_box(ro, c)
            x = check_cell(ro, c, b)

    ran = get_box_range(bo)

    for r in ran[0] :
        for(c in ran[1]):
            if(lst[r][c][1] == '-'):
                b = val_box(r, c)
                x = check_cell(r, c, b)
