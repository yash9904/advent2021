from statistics import mode

with open('day3\input.txt') as f:
    k = f.read().split('\n')

gamma = ''
epsilon = ''

size = len(k[0])


for i in range(size):
    gamma += str(mode([g[i: i + 1] for g in k]))

for i in gamma:
    if i == '0':
        epsilon += '1'
    else:
        epsilon += '0'

eps_int = 0
gam_int = 0

for i in range(size):
    if gamma[i: i + 1] == '0':
        pass
    elif gamma[i: i + 1] == '1':
        gam_int += pow(2, size - i - 1)
    if epsilon[i: i + 1] == '0':
        pass
    elif epsilon[i: i + 1] == '1':
        eps_int += pow(2, size - i - 1)

print(gam_int * eps_int)