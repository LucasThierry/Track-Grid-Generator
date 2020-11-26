from random import randint
import argparse

def arguments_definition():
    """
    Method for creating the possible parameters for execution.
    :return ArgumentParser:
    """
    parser = argparse.ArgumentParser(description='Runs the track gen.')
    parser.add_argument(
        '--preset', '-p',
        type=str,
        choices=['straight', '90', '45', 'random', 'custom'],
        default='random',
        help='Setup a track type tendency.')

    parser.add_argument(
        '--size', '-s',
        type=int,
        nargs=1,
        default=8,
        help='Choose track size (for now only >=8)')

    parser.add_argument(
        '--density', '-d',
        type=int,
        nargs=1,
        default=24,
        help='Choose track density')
    return parser.parse_args()

def run():
    args = arguments_definition()
    print(args.size)
    grid = []
    # Create a 8x8 grass grid
    for row in range(args.size[0]):
        grid.append([])
        for col in range(args.size[0]):
            grid[row].append(" ")

    # Setup initial asphalt tiles

    s = args.size[0]
    s2 = int(s/2)
    s4 = int(s/4)
    print(s)
    print(s2)

    if args.preset == 'straight':
        grid [s2-1][0] = "☐"
        grid [s2][0] = "☐"
        grid [s2-1][s2-1] = "☐"
        grid [s2][s2] = "☐"
        grid [s2-1][s-1] = "☐"
        grid [s2][s-1] = "☐"
            
    elif args.preset == '90':
        grid [0][s2-1] = "☐"
        grid [0][s2] = "☐"
        grid [s2-1][s2-1] = "☐"
        grid [s2][s2] = "☐"
        grid [s2-1][s-1] = "☐"
        grid [s2][s-1] = "☐"

    elif args.preset == '45':
        grid [0][s4-1] = "☐"
        grid [0][s4-2] = "☐"
        grid [s2-1][s2-1] = "☐"
        grid [s2][s2] = "☐"
        grid [s4+s2-3][s-1] = "☐"
        grid [s4+s2-2][s-1] = "☐"

    elif args.preset == 'random':
        grid [0][0] = "☐"
        grid [0][1] = "☐"
        grid [1][0] = "☐"
        grid [s-1][s-1] = "☐"
        grid [s-2][s-1] = "☐"
        grid [s-1][s-2] = "☐"
        grid [0][s-1] = "☐"
        grid [1][s-1] = "☐"
        grid [0][s-2] = "☐"
        grid [s-1][0] = "☐"
        grid [s-1][1] = "☐"
        grid [s-2][0] = "☐"

    elif args.preset == 'dia':
        grid [0][0] = "☐"
        grid [0][1] = "☐"
        grid [1][0] = "☐"
        grid [s-1][s-1] = "☐"
        grid [s-2][s-1] = "☐"
        grid [s-1][s-2] = "☐"

    elif args.preset == 'custom':
        q = int(input("Quantos pontos inicias? "))
        for qty in range(q):
            x = int(input("Coordenada X: "))
            y = int(input("Coordenada Y: "))
            grid [x][y] = "☐"
            
    
    # Range sets asphalt units quantity
    for asphalts in range(args.density[0]):
        c_x = randint(1, len(grid)-2)
        c_y = randint(1, len(grid[0])-2)
        while (grid[c_x+1][c_y] == " ") and (grid[c_x][c_y+1] == " ") and (grid[c_x-1][c_y] == " ") and (grid[c_x][c_y-1] == " ") and (grid[c_x][c_y] == "☐"):
            c_x = randint(0, len(grid) - 2)
            c_y = randint(0, len(grid[0]) - 2)
        grid[c_x][c_y] = "☐"

    for n in range (s):
        print(grid[n])

if __name__ == '__main__':
    run()