fileName = 'input.txt'
fileHandle = open(fileName)

dir = fileHandle.readline()
dir = dir[:-1]


nodes = [x.strip('\n') for x in fileHandle.readlines()[1:]]

dic = {}

steps_list = []

for temp in nodes:
    x = temp.split()
    dic[x[0]] = (x[2][1:-1], x[3][:-1])
directions = {'R': 1, 'L': 0}

def do(n):
    steps = 0
    x = 0 # for the left and right loop

    while True:
        try:
            index = directions[dir[x]]
            n = dic[n][index]

            steps += 1
            x += 1

            if n[-1] == 'Z':
                break

        except IndexError:
            x = 0
            continue
    return steps


for n in dic.keys():
    if (n[-1]) == 'A':
        steps_list.append(do(n))

print(steps_list)





