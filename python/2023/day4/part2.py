fileName = 'input.txt'
fileHandle = open(fileName)

lines = fileHandle.readlines()

line = [x[:-1] for x in lines[:-1]]

gameNum = {}
for x in range(1, len(line) + 1):
    gameNum[x] = 1

answer = 0
cur = 1
for x in line:
    temp = x.split(':')[-1].split('|')
    number = temp[-1].split()
    numbers = [int(z) for z in number]
    count = 0
    for m in temp[0].split():
        if int(m) in numbers:
            count += 1
    if count > 0:
        answer += 2 ** (count - 1)
        for num in range(count):
            gameNum[num + 1 + cur] += 1*gameNum[cur]
    cur += 1
print(gameNum)
print('part1 ', answer)
print('part2', sum(gameNum.values()))