fileName = 'input.txt'

fileHandle = open(fileName)
input = fileHandle.readlines()

lines = [line[:-1] for line in input[:-1]]

sym = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']

length_rows = len(lines)
length_cols = len(lines[0])

pos_1 = []
justNum = {}
index = 0
pos, num, n = [], 0, -1
for line in range(length_rows):
    for x in zip(lines[line][::-1], range(length_cols-1,-1,-1)):
        if x[0] in sym[:-1]:
            n += 1
            num += int(x[0])*(10**n)
            pos.append((line,x[1]))
        elif pos != []:
            justNum[index] = num
            pos_1.append(pos)
            index += 1
            pos, num, n = [], 0, -1

dir = [(0,-1),(0,1),(1,0),(-1,0),(-1,-1),(1,1),(1,-1),(-1,1)]

def valid(row,col):
    hi = [(row+d[0], col+d[1]) for d in dir]
    return hi

possible = []
for line in range(length_rows):
    for char in range(length_cols):
        if lines[line][char] not in sym:
            things = valid(line,char)
            for thing in things:
                if lines[thing[0]][thing[1]] in sym[:-1]:
                    possible.append((thing[0],thing[1]))
print(possible)

print(pos_1)
print(justNum)
answer = 0
for x in possible:
    for m in zip(pos_1, range(len(pos_1))):
        if x in m[0]:
            print(justNum[m[1]], end=' ')
            answer += justNum[m[1]]
            pos_1[m[1]] = []
            break

print()
print(answer)






