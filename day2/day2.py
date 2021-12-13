with open('day2\input.txt', 'r') as f:
    k = f.read().split('\n')

x = 0
y = 0

aim = 0

for i in k:
    temp = i.split(' ')
    
    if temp[0] == 'forward':
        x += int(temp[1])
        y += aim * int(temp[1])
    elif temp[0] == 'up':
        aim += int(temp[1])
    elif temp[0] == 'down':
        aim -= int(temp[1])

print(x * y)