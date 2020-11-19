from random import randint
import argparse

def arguments_definition():
    """
    Method for creating the possible parameters for execution.
    :return ArgumentParser:
    """
    parser = argparse.ArgumentParser(description='Runs the track gen.')
    parser.add_argument(
        'preset',
        type=str,
        choices=['straight', '90', '45', 'random'],
        help='Setup a track type tendency.')

    return parser.parse_args()

def run():
    args = arguments_definition()

    grid = []
    # Create a 8x8 grass grid
    for row in range(8):
        grid.append([])
        for col in range(8):
            grid[row].append(" ")

    # Setup initial asphalt tiles
    if args.preset == 'straight':
        grid [3][0] = "☐"
        grid [4][0] = "☐"
        grid [3][3] = "☐"
        grid [4][4] = "☐"
        grid [3][7] = "☐"
        grid [4][7] = "☐"
            
    elif args.preset == '90':
        grid [0][3] = "☐"
        grid [0][4] = "☐"
        grid [3][3] = "☐"
        grid [4][4] = "☐"
        grid [3][7] = "☐"
        grid [4][7] = "☐"

    elif args.preset == '45':
        grid [0][1] = "☐"
        grid [0][2] = "☐"
        grid [3][3] = "☐"
        grid [4][4] = "☐"
        grid [5][7] = "☐"
        grid [6][7] = "☐"

    elif args.preset == 'random':
        grid [0][0] = "☐"
        grid [0][1] = "☐"
        grid [1][0] = "☐"
        grid [7][7] = "☐"
        grid [6][7] = "☐"
        grid [7][6] = "☐"
        grid [0][7] = "☐"
        grid [1][7] = "☐"
        grid [0][6] = "☐"
        grid [7][0] = "☐"
        grid [7][1] = "☐"
        grid [6][0] = "☐"

    elif args.preset == 'dia':
        grid [0][0] = "☐"
        grid [0][1] = "☐"
        grid [1][0] = "☐"
        grid [7][7] = "☐"
        grid [6][7] = "☐"
        grid [7][6] = "☐"
            
    
    # Range sets asphalt units quantity
    for asphalts in range(24):
        c_x = randint(1, len(grid)-2)
        c_y = randint(1, len(grid[0])-2)
        while (grid[c_x+1][c_y] == " ") and (grid[c_x][c_y+1] == " ") and (grid[c_x-1][c_y] == " ") and (grid[c_x][c_y-1] == " "):
            c_x = randint(0, len(grid) - 2)
            c_y = randint(0, len(grid[0]) - 2)
        grid[c_x][c_y] = "☐"

    for n in range (8):
        print(grid[n])

if __name__ == '__main__':
    run()