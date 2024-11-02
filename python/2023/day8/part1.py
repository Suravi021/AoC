fileName = 'input.txt'
fileHandle = open(fileName)

dir = fileHandle.readline()
dir = dir[:-1]

nodes = [x.strip('\n') for x in fileHandle.readlines()[1:]]

dic = {}

for temp in nodes:
    x = temp.split()
    dic[x[0]] = (x[2][1:-1],x[3][:-1])
directions = {'R':1, 'L':0}

print(dic)

x = 0
steps = 0
stop = False
node = 'AAA'
while True:
    try:
        index = directions[dir[x]]
        node = dic[node][index]
        steps += 1
        print(node)
        if node == 'ZZZ':
            stop = True
        if stop:
            break
        x += 1
    except IndexError:
        x = 0
        continue
print(steps)



