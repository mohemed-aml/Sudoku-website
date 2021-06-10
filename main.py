# list, row, column and box initalizations
lst = [ [ [ False, '-', [], 0 ] for col in range(9)] for row in range(9)]
row = [[ False, 9, [c for c in range(1, 10)] ] for r in range(9)]
col = [[ False, 9, [c for c in range(1, 10)] ] for r in range(9)]
box = [[ False, 9, [c for c in range(1, 10)] ] for r in range(9)]

# function to find out box number
def val_box(ro, co):
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
    bo -= 1
    return bo
# function to set a value to a position
def set_val(ro, co, val):

    bo = val_box(ro, co)

    lst[ro][co][1] = val
    lst[ro][co][0] = True
    lst[ro][co][2].clear()

    row[ro][1] -= 1
    row[ro][2].remove(val)
    if ( row[ro][1] == 0):
        row[ro][0] = True

    col[co][1] -= 1
    col[co][2].remove(val)
    if ( col[co][1] == 0):
        col[co][0] = True

    box[bo][1] -= 1
    box[bo][2].remove(val)
    if ( box[bo][1] == 0):
        box[bo][0] = True
# function to print the sudoku
def print_sudoku():
    print('\n\n\n\n')
    print('                ___________ ___________ ___________',)
    print('               |           |           |           |')
    print('               | ',lst[0][0][1], '', lst[0][1][1], '', lst[0][2][1], ' | ', lst[0][3][1], '', lst[0][4][1], '', lst[0][5][1], ' | ', lst[0][6][1], '', lst[0][7][1], '', lst[0][8][1], ' |')
    print('               | ',lst[1][0][1], '', lst[1][1][1], '', lst[1][2][1], ' | ', lst[1][3][1], '', lst[1][4][1], '', lst[1][5][1], ' | ', lst[1][6][1], '', lst[1][7][1], '', lst[1][8][1], ' |')
    print('               | ',lst[2][0][1], '', lst[2][1][1], '', lst[2][2][1], ' | ', lst[2][3][1], '', lst[2][4][1], '', lst[2][5][1], ' | ', lst[2][6][1], '', lst[2][7][1], '', lst[2][8][1], ' |')
    print('               |___________|___________|___________|')
    print('               |           |           |           |')
    print('               | ',lst[3][0][1], '', lst[3][1][1], '', lst[3][2][1], ' | ', lst[3][3][1], '', lst[3][4][1], '', lst[3][5][1], ' | ', lst[3][6][1], '', lst[3][7][1], '', lst[3][8][1], ' |')
    print('               | ',lst[4][0][1], '', lst[4][1][1], '', lst[4][2][1], ' | ', lst[4][3][1], '', lst[4][4][1], '', lst[4][5][1], ' | ', lst[4][6][1], '', lst[4][7][1], '', lst[4][8][1], ' |')
    print('               | ',lst[5][0][1], '', lst[5][1][1], '', lst[5][2][1], ' | ', lst[5][3][1], '', lst[5][4][1], '', lst[5][5][1], ' | ', lst[5][6][1], '', lst[5][7][1], '', lst[5][8][1], ' |')
    print('               |___________|___________|___________|')
    print('               |           |           |           |')
    print('               | ',lst[6][0][1], '', lst[6][1][1], '', lst[6][2][1], ' | ', lst[6][3][1], '', lst[6][4][1], '', lst[6][5][1], ' | ', lst[6][6][1], '', lst[6][7][1], '', lst[6][8][1], ' |')
    print('               | ',lst[7][0][1], '', lst[7][1][1], '', lst[7][2][1], ' | ', lst[7][3][1], '', lst[7][4][1], '', lst[7][5][1], ' | ', lst[7][6][1], '', lst[7][7][1], '', lst[7][8][1], ' |')
    print('               | ',lst[8][0][1], '', lst[8][1][1], '', lst[8][2][1], ' | ', lst[8][3][1], '', lst[8][4][1], '', lst[8][5][1], ' | ', lst[8][6][1], '', lst[8][7][1], '', lst[8][8][1], ' |')
    print('               |___________|___________|___________|')
    print('\n\n\n')
# function to find if row colun or box has least number of elements
def small(a, b, c):
    if(a < b):
        if(a < c):
            return('r')
        else:
            return('b')
    else:
        if (b < c):
            return('c')
        else:
            return('b')
# function to return the range for row and column of a box position
def get_box_range(bo):

    if (bo == 0):
        return ([ [0, 1, 2], [0, 1, 2] ])
    elif (bo == 1):
        return ([ [0, 1, 2], [3, 4, 5] ])
    elif (bo == 2):
        return ([ [0, 1, 2], [6, 7, 8] ])
    elif (bo == 3):
        return ([ [3, 4, 5], [0, 1, 2] ])
    elif (bo == 4):
        return ([ [3, 4, 5], [3, 4, 5] ])
    elif (bo == 5):
        return ([ [3, 4, 5], [6, 7, 8] ])
    elif (bo == 6):
        return ([ [6, 7, 8], [0, 1, 2] ])
    elif (bo == 7):
        return ([ [6, 7, 8], [3, 4, 5] ])
    else:
        return ([ [6, 7, 8], [6, 7, 8] ])
# function to check possible values in a cell
def check_cell(ro, co, bo):

    r = row[ro][1]
    c = col[co][1]
    b = box[bo][1]
    sm = small(r, c, b)

    if ( sm == 'r'):
        for el in row[ro][2]:
            if( (el in col[co][2]) and (el in box[bo][2]) ):
                lst[ro][co][2].append(el)
                lst[ro][co][3] += 1

    if ( sm == 'c'):
        for el in col[co][2]:
            if( (el in row[ro][2]) and (el in box[bo][2]) ):
                lst[ro][co][2].append(el)
                lst[ro][co][3] += 1

    if ( sm == 'b'):
        for el in box[bo][2]:
            if( (el in col[co][2]) and (el in row[ro][2]) ):
                lst[ro][co][2].append(el)
                lst[ro][co][3] += 1

    if ( lst[ro][co][3] == 1):
        set_val( ro, co, lst[ro][co][2][0] )
        print_sudoku()
        check_related_cells(ro, co, bo)
        check_row(ro)
        check_col(co)
        check_box(bo)
        return True

    return False
# function to check a particular row
def check_row(ro):
    flag = False
    for val in row[ro][2]:
        count = 0
        pos = 0
        for co in range(9):
            if( lst[ro][co][1] == '-' ):
                if( val in lst[ro][co][2]):
                    count += 1
                    pos = co
        if ( count == 1 ):
            set_val(ro, pos, val)
            print_sudoku()
            bo = val_box(ro, pos)
            check_related_cells(ro, co, bo)
            check_row(ro)
            check_col(co)
            check_box(bo)
            flag = True
    return flag
# function to check a particular column
def check_col(co):
    flag = False
    for val in col[co][2]:
        count = 0
        pos = 0
        for ro in range(9):
            if( lst[ro][co][1] == '-' ):
                bo = val_box(ro, co)
                if( val in lst[ro][co][2]):
                    count += 1
                    pos = ro
        if ( count == 1 ):
            set_val(pos, co, val)
            print_sudoku()
            bo = val_box(pos, co)
            check_related_cells(ro, co, bo)
            check_row(ro)
            check_col(co)
            check_box(bo)
            flag = True
    return flag
# function to check a particular box
def check_box(bo):
    flag = False
    for val in box[bo][2]:
        ran = get_box_range(bo)
        count = 0
        pos = []
        for r in ran[0] :
            for c in ran[1] :
                if(lst[r][c][1] == '-'):
                    if ( val in lst[r][c][2] ):
                        count += 1
                        pos.append(r)
                        pos.append(c)
        if ( count == 1 ):
            set_val(pos[0], pos[1], val)
            print_sudoku()
            bo = val_box(pos[0], pos[1])
            check_related_cells(pos[0], pos[1], bo)
            check_row(pos[0])
            check_col(pos[1])
            check_box(bo)
            flag = True
    return flag
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
        for c in ran[1] :
            if(lst[r][c][1] == '-'):
                b = val_box(r, c)
                x = check_cell(r, c, b)
# function to enter initial values into the sudoku
def initial_value():
    choice1 = input("Eneter values manually?(y/n)")
    if (choice1 == 'y'):
        flag1 = True
        flag2 = True
        while(flag1):
            while(flag2):
                r = input("Enter row position: ")
                c = input("Enter col position: ")
                v = input("Enter value: ")
                ro = int(r)
                co = int(c)
                val = int(v)
                ro -= 1
                co -= 1
                set_val(ro, co, val)
                choice = input("Is there another value?(y/n)")
                if(choice == "n"):
                    flag2 = False
            print_sudoku()
            ch = input("Is there any change to be made to the puzzle?(y/n)")
            if(ch == "n"):
                flag1 = False
    else:
        set_val(0, 0, 9)
        set_val(0, 1, 4)
        set_val(0, 3, 5)
        set_val(0, 6, 6)
        set_val(1, 6, 4)
        set_val(1, 8, 2)
        set_val(2, 3, 7)
        set_val(2, 5, 3)
        set_val(2, 6, 5)
        set_val(2, 8, 9)
        set_val(3, 0, 1)
        set_val(3, 4, 9)
        set_val(3, 8, 5)
        set_val(4, 2, 5)
        set_val(4, 4, 6)
        set_val(4, 6, 1)
        set_val(5, 0, 8)
        set_val(5, 4, 3)
        set_val(5, 8, 4)
        set_val(6, 0, 4)
        set_val(6, 2, 7)
        set_val(6, 3, 3)
        set_val(6, 5, 2)
        set_val(7, 0, 5)
        set_val(7, 2, 9)
        set_val(8, 2, 1)
        set_val(8, 5, 9)
        set_val(8, 7, 2)
        set_val(8, 8, 7)
        print_sudoku()
# function to go through each cell in the suduku
def go_through_cell():
    count2 = 0
    flag1 = True
    while(flag1):
        count = 0
        count2 += 1
        for ro in range(9):
            for co in range(9):
                if( lst[ro][co][1] == '-'):
                    bo = val_box(ro, co)
                    flag2 = check_cell(ro, co, bo)
                    if (flag2):
                        count += 1
        if ( count == 0):
            flag1= False
    if( count2 == 1):
        return False
    else:
        return True
# function to go through each row in the sudoku
def go_through_row():
    count2 = 0
    flag1 = True
    while(flag1):
        count = 0
        for ro in range(9):
            if ( row[ro][0] == False ):
                flag2 = check_row(ro)
                if (flag2):
                    count += 1
        if ( count == 0):
            flag1 = False
    if ( count2 == 1 ):
        return False
    else:
        return True
# function to go through each column in the sudoku
def go_through_col():
    count2 = 0
    flag1 = True
    while(flag1):
        count = 0
        for co in range(9):
            if ( col[co][0] == False ):
                flag2 = check_col(co)
                if (flag2):
                    count += 1
        if ( count == 0):
            flag1 = False
    if ( count2 == 1 ):
        return False
    else:
        return True
# function to go through each row in the sudoku
def go_through_box():
    count2 = 0
    flag1 = True
    while(flag1):
        count = 0
        for bo in range(9):
            if ( box[bo][0] == False ):
                flag2 = check_box(bo)
                if (flag2):
                    count += 1
        if ( count == 0):
            flag1 = False
    if ( count2 == 1 ):
        return False
    else:
        return True

initial_value()
flag = True
copy = []
while(flag):
    copy.clear()
    copy.extend(lst)
    flag = False
    flag1 = go_through_cell()
    flag2 = go_through_row()
    flag3 = go_through_col()
    flag4 = go_through_box()
    if ( check_row(4) ):
        print('hi')
    else:
        print(lst[4][5][2])
    if ( copy == lst):
        flag = False
print_sudoku()
