fileName = 'input.txt'
fileHandle = open(fileName)

data = [x.strip('\n') for x in fileHandle.readlines()]

def transpose(matrix):
    x = len(matrix[0])
    y = len(matrix)
    new_matrix = []
    for n in range(x):
        row = ''
        for m in range(y):
            row += str(matrix[m][n])
        new_matrix.append(row)
    return new_matrix

def check(matrix, extra):
    things = []
    for x in range(len(matrix)):
        if matrix[x] == extra:
            things.append(x+1)
    d = 0
    for x in things:
        matrix.insert(x+d,extra)
        d += 1
    return None

check(data, '.'*len(data[0])) # adds rows
x = transpose(data) # rows should get converted to columns

check(x, '.'*len(x[0])) # should add rows but are actually cols
data = transpose(x)

pos = []
for x in range(len(data)):
    for y in range(len(data[0])):
        if data[x][y] == '#':
            pos.append((x+1,y+1))
step = -1
answer = 0
for x in pos[:-1]:
    step += 1
    for y in pos[step:]:
        if x == y:
            continue
        answer += abs(x[0]-y[0]) + abs(x[1]-y[1])
print(answer)





