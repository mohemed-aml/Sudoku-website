# list, row, column and box initalizations
lst = [ [ [ False, '-', [], 0 ] for col in range(9)] for row in range(9)]
row = [[ False, 9, [c for c in range(1, 10)] ] for r in range(9)]
col = [[ False, 9, [c for c in range(1, 10)] ] for r in range(9)]
box = [[ False, 9, [c for c in range(1, 10)] ] for r in range(9)]

print(row)
