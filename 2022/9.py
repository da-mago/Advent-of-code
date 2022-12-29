import numpy as np
import sys

def getAction(where):
    if where == 'D':
        return [-1,  0]
    elif where == 'U':
        return [ 1,  0]
    elif where == 'R':
        return [ 0,  1]
    elif where == 'L':
        return [ 0, -1]

    print("Invalid action")
    sys.exit()

def tailMove(T, H):
    ty,tx = T
    hy,hx = H

    if abs(hx - tx) == 2:
        if (hx - tx) > 0:
            T += getAction('R')
        else:
            T += getAction('L')

        if   (hy - ty) == 1:
            T += getAction('U')
        elif (hy - ty) == -1:
            T += getAction('D')

    if abs(hy - ty) == 2:
        if (hy - ty) > 0:
            T += getAction('U')
        else:
            T += getAction('D')

        if   (hx - tx) == 1:
            T += getAction('R')
        elif (hx - tx) == -1:
            T += getAction('L')

    return T

# Read input
lines = open("9.in").readlines()

moves = [[line.split(' ')[0], int(line.split(' ')[1])] for line in lines]

moves_len = len(moves)
# Create grid bug enough to keep 'moves_len' in one direction 
# assuming you start in the middle of the grid
grid_1 = np.zeros((2*moves_len, 2*moves_len), dtype=np.uint8)
# Initial locations
num_T = 10
T_all = [np.array([moves_len, moves_len]) for _ in range(num_T)]
grid_1[tuple(T_all[0])] = 1
grid_2 = grid_1.copy()
# helper
for move in moves:
    where, steps = move
    for step in range(steps):
        action = getAction(where)
        # Update Head
        T_all[0] += action
        # Update tails
        for i in range(1, num_T):
            T_all[i] = tailMove(T_all[i], T_all[i-1])
        grid_1[tuple(T_all[1])] = 1
        grid_2[tuple(T_all[num_T - 1])] = 1

print("Part 1", sum(sum(grid_1)))
print("Part 2", sum(sum(grid_2)))
