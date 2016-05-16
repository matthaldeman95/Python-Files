import numpy as np

def genSquare(row, col):
    if row < 3: rows = [0, 1, 2]
    if row > 2 and row < 6: rows = [3, 4, 5]
    if row > 5 and row < 9: rows = [6, 7, 8]
    if col < 3: cols = [0,1,2]
    if col > 2 and col < 6: cols = [3,4,5]
    if col > 5 and col < 9: cols = [6,7,8]

    return rows, cols

def isValid(grid, row, col, val):

    rows, cols = genSquare(row, col)
    for n in range(0,9):    #Check column
        if val == grid[n, col]: return False
        if val == grid[row, n]: return False
    for r in rows:
        for c in cols:
            if val == grid[r,c]: return False
    else: return True

def tryValue(grid,row,col,val):
    if grid[row,col] == 0:
        if isValid(grid,row,col,val) == True:
            #grid[row,col] = val
            print "Row: %d, Column: %d, Value: %s" % (row,col,val)
            return True
        else: return False
    else:
        return grid[row,col]


line0 = '0 0 4 0 8 0 3 0 0'
line1 = '0 0 0 0 0 3 0 4 2'
line2 = '8 0 0 4 0 5 9 0 7'
line3 = '3 0 2 0 7 0 5 0 8'
line4 = '0 5 0 0 0 0 0 7 0'
line5 = '6 0 8 0 9 0 2 0 1'
line6 = '4 0 6 2 0 7 0 0 9'
line7 = '5 2 0 9 0 0 0 0 0'
line8 = '0 0 7 0 1 0 4 0 0'

"""
1 6 4 7 8 2 3 5 0
0 0 0 0 0 3 0 4 2
8 0 0 4 0 5 9 0 7
3 0 2 0 7 0 5 0 8
0 5 0 0 0 0 0 7 0
6 0 8 0 9 0 2 0 1
4 0 6 2 0 7 0 0 9
5 2 0 9 0 0 0 0 0
0 0 7 0 1 0 4 0 0
"""

a = np.matrix('%s ;%s ;%s ;%s ;%s; %s; %s; %s; %s' % (line0, line1, line2, line3, line4, line5, line6, line7, line8))




def solve(grid,r,c,val):
    var = tryValue(grid,r,c,val)
    if var == True:
        grid[r,c] = val
        if c<9:
            solve(grid,r,c+1,1)
        else:
            solve(grid,r+1,0,1)
    elif var == False:
        if val<9:
            solve(grid,r,c,val+1)
        else:
            print r, c-1, grid[r,c-1]
            solve(grid,r,c-1,(grid[r,c-1]+1))
    else:
        solve(grid,r,c+1,1)




solve(a,0,0,1)

print a