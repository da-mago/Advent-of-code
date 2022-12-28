# Read input
lines = open("2.in") .readlines()

score1 = 0
score2 = 0
score_table = [3, 6, 0, 0, 3, 6, 6, 0, 3]
for line in lines:
    data = line.strip().split()
    data[0] = ord(data[0]) - ord('A')
    data[1] = ord(data[1]) - ord('X')

    # Part 1
    game_score = score_table[data[0]*3 + data[1]]
    my_score   = data[1] + 1
    score1 += my_score + game_score

    # Part 2
    game_score = 3*data[1]
    sub_table  = score_table[3*data[0]:3*data[0]+3]
    if game_score == 0:   # loose
        my_score = sub_table.index(0) + 1
    elif game_score == 3: # draw
        my_score = sub_table.index(3) + 1
    else:
        my_score = sub_table.index(6) + 1
    score2 += my_score + game_score

print("Part 1: ",score1)
print("Part 2: ",score2)
    


