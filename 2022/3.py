# Read input
lines = [x.strip() for x in open("3.in").readlines()]

priorities = 0
for line in lines:
    c_len = int(len(line)/2)
    #print(c_len)
    c1 = line[0:c_len]
    c2 = line[c_len:]
    for c in line[0:c_len]:
        if c in line[c_len:]:
            if c < 'a':
                val = ord(c) - ord('A') + 27
            else:
                val = ord(c) - ord('a') + 1
            priorities += val
            break
print("Part 1", priorities)

priorities = 0
for i in range(len(lines)//3):
    items = ''
    str1 = lines[i*3]
    str2 = lines[i*3 + 1]
    str3 = lines[i*3 + 2]
    for c in str1:
        if c in str2 and c in str3:
            if c < 'a':
                val = ord(c) - ord('A') + 27
            else:
                val = ord(c) - ord('a') + 1
            priorities += val
            items += c
            break
        

print("Part 2", priorities)

