from random import randint

grid = []
# Create a 8x8 grass grid
for row in range(8):
    grid.append([])
    for col in range(8):
        grid[row].append(" ")

# Setup initial asphalt tiles

grid [0][0] = "☐"
#grid [0][7] = "☐"
grid [7][7] = "☐"
#grid [7][0] = "☐"

# Range sets asphalt units quantity
for asphalts in range(36):
    c_x = randint(1, len(grid)-2)
    c_y = randint(1, len(grid[0])-2)
    while (grid[c_x+1][c_y] == " ") and (grid[c_x][c_y+1] == " ") and (grid[c_x-1][c_y] == " ") and (grid[c_x][c_y-1] == " ") and (grid[c_x+1][c_y+1] == " ") and (grid[c_x-1][c_y+1] == " ") and (grid[c_x-1][c_y-1] == " ") and (grid[c_x+1][c_y-1] == " "):
        c_x = randint(0, len(grid) - 2)
        c_y = randint(0, len(grid[0]) - 2)
    grid[c_x][c_y] = "☐"

for n in range (8):
    print(grid[n])