import sys

# Read input
filename = sys.argv[0].split('.')[0] + '.in'
line = open(filename).read()

for j, marker_size in enumerate([4, 14]):
    for i in range(len(line) - (marker_size - 1)):
        if len(set(line[i:i+marker_size])) == marker_size:
            idx = i
            break
    print("Part {} {}".format(j+1, marker_size + idx))
    
