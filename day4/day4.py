with open('day4/input.txt', 'r') as f:
    k = f.read().split('\n')

num_list = k[0]

bingo_grids = []

for i in range(1, len(k)):
    if i % 6 == 1:
        bingo_grids.append(k[i + 1: i + 6])

print(bingo_grids[0])