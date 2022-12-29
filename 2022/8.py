import numpy as np
import sys

# Read input
filename = sys.argv[0].split('.')[0] + '.in'
lines = [x.strip() for x in open(filename)]

row_len = len(lines[0])
col_len = len(lines)
tree_map = []
for row in lines:
    tree_row = [int(row[i]) for i in range(row_len)]
    tree_map.append(tree_row)


np_map = np.array(tree_map)

r_len = len(np_map[0])
c_len = len(np_map)
# Add all boundary trees
total_1 = r_len*2 + (c_len-2)*2
total_2 = 0
# Add internal trees
for i in range(1, r_len-1):
    for j in range(1, c_len-1):
        # Part 1
        if np_map[i][j] > np.max(np_map[0:i ,j])    or \
           np_map[i][j] > np.max(np_map[i+1:,j])    or \
           np_map[i][j] > np.max(np_map[i   ,0:j])  or \
           np_map[i][j] > np.max(np_map[i   ,j+1:]):
            total_1 += 1

        # Part 2
        all_size = []
        size = 0
        for k in range(i-1, -1, -1):
            size += 1
            if np_map[k ,j] >= np_map[i,j]:
                break
        all_size.append(size)

        size = 0
        for k in range(i+1, r_len):
            size += 1
            if np_map[k ,j] >= np_map[i,j]:
                break
        all_size.append(size)

        size = 0
        for k in range(j-1, -1, -1):
            size += 1
            if np_map[i ,k] >= np_map[i,j]:
                break
        all_size.append(size)

        size = 0
        for k in range(j+1, r_len):
            size += 1
            if np_map[i ,k] >= np_map[i,j]:
                break
        all_size.append(size)

        res = 1
        for t in all_size:
            res *= t
        if res > total_2:
            total_2 = res

print("Part 1", total_1)
print("Part 2", total_2)
