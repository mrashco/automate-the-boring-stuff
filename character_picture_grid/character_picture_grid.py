# Character Picture Grid

# Take grid
# Loop through
# Chage order of output [x][y]
#   [8][0] goes first
#   Loop through indexes
# Print out new result


grid = [['.', '.', '.', '.', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def main(): draw(grid)

def draw(l):
    row, column = 8, 0 # Start in bottom left of grid list
    for i in l: # Loop through lists in grid
        for j in l: # Loop through items in each list
            print(l[row][column], end='') # Print out as per starting point
            row -= 1 # Reverse up the column, results in row output
        if column < 5: # Go until row 6 (0-5)
            row = 8 # Reset column back to the bottom or last
            column += 1 # Move up a row to being new row
            print('') # Print new line
        else: break # Once greater than 6th row, break and exit out

if __name__ == '__main__': main()