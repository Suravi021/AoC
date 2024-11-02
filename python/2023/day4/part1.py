fileName = 'input.txt'
fileHandle = open(fileName)

lines = fileHandle.readlines()

line = [x[:-1] for x in lines[:-1]]

gameNum = 0
answer = 0

for x in line:
    temp = x.split(':')[-1].split('|')
    number = temp[-1].split()
    numbers = [int(z) for z in number]
    count = 0
    for m in temp[0].split():
        if int(m) in numbers:
            count += 1
    if count > 0:
        answer += 2 ** (count-1)

print('part1 ',answer)

