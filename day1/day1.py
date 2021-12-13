
with open('input.txt', 'r') as f:
    k = f.read()
t = k.split('\n')

t = [int(t[i]) for i in range(2000)]

count = 0

print(len(t))

for i in range(0, 2000):
    if sum(t[i + 1: i + 4]) > sum(t[i: i + 3]):
        count += 1
print(count)