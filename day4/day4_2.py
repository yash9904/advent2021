import numpy as np

with open('day4/input.txt', 'r') as f:
    k = f.read().split('\n')

num_list = [int(num) for num in k[0].split(',')]

bingo_grids = []

for i in range(1, len(k)):
    if i % 6 == 1:
        bingo_grids.append(k[i + 1: i + 6])

bingo_grids = bingo_grids[: -1]

for i in range(len(bingo_grids)):
    for k in range(5):
        bingo_grids[i][k] = bingo_grids[i][k].strip(' ').split(' ')
        for p in range(5):
            if bingo_grids[i][k][p] == '':
                bingo_grids[i][k] =  bingo_grids[i][k][: p] + bingo_grids[i][k][p + 1:]

for i in range(len(bingo_grids)):
    for k in range(5):
        bingo_grids[i][k] = [int(i) for i in bingo_grids[i][k]]

num_called = list()

bingo_grids = np.array(bingo_grids)

flag = False

winner_indices = []

for num in num_list:
    for i in range(len(bingo_grids)):
        if i not in winner_indices:
            for j in range(5):
                if sum([test in num_called for test in bingo_grids[i][j]]) == 5:
                    last_num = num_called[-1]
                    winner_indices.append(i)
                    break
                if sum([test in num_called for test in bingo_grids[i, :, j]]) == 5:
                    last_num = num_called[-1]
                    winner_indices.append(i)
                    break

    num_called.append(num)

num_called = np.array(num_called)

winner_board = bingo_grids[winner_indices[-1]]
score = 0
last_num_index = np.where(num_called == last_num)[0][0]
flattened_board = np.ravel(winner_board)

for i in range(len(flattened_board)):
    if flattened_board[i] not in num_list[: last_num_index + 1]:
        score += flattened_board[i]

print(score * last_num)