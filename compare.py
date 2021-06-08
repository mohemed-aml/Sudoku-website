#list initalization
lst = [ [ [ False, '-', [], 0 ] for col in range(9)] for row in range(9)]

#row array definition
row = [[ False, 9, [c for c in range(1, 10)] ] for r in range(9)]

#column array definition
col = [[ False, 9, [c for c in range(1, 10)] ] for r in range(9)]

#box array definition
box = [[ False, 9, [c for c in range(1, 10)] ] for r in range(9)]

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

def check_cell(ro, co, bo):

    r = row[ro][1]
    c = col[co][1]
    b = box[bo][1]
    sm = small(r, c, b)

    if ( sm == 'r'):
        for el in row[ro][2]:
            if( (el in col[co][2]) && (el in box[bo][2]) ):
                lst[ro][co][2].append(el)
                lst[ro][co][3] += 1

    if ( sm == 'c'):
        for el in col[co][2]:
            if( (el in row[ro][2]) && (el in box[bo][2]) ):
                lst[ro][co][2].append(el)
                lst[ro][co][3] += 1

    if ( sm == 'b'):
        for el in box[bo][2]:
            if( (el in col[co][2]) && (el in row[ro][2]) ):
                lst[ro][co][2].append(el)
                lst[ro][co][3] += 1

    if ( lst[ro][co][3] == 1):
        set_val(ro, co, bo)
        print_sudoku()




def check_row(ro):


def check_col(co):


def check_box(bo):
