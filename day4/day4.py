import numpy as np

with open('day4/input.txt', 'r') as f:
    k = f.read().split('\n')

num_list = k[0].split(',')
num_list = [int(num) for num in num_list]


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

for num in num_list:
    for i in range(len(bingo_grids)):
        for j in range(5):
            if sum([test in num_called for test in bingo_grids[i][j]]) == 5:
                answer = i
                print('board found!!')
                flag = True
                break
            if sum([test in num_called for test in bingo_grids[i, :, j]]) == 5:
                answer = i
                print('board found!!')
                flag = True
                break
        if flag:
            break
    if flag:
        break

    num_called.append(num)


winner_board = bingo_grids[answer]

print(winner_board)

score = 0

for i in np.ravel(winner_board):
    if i not in num_called:
        score += i

print(score * num_called[-1])