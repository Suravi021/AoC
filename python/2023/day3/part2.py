import sys

fileName = sys.argv[1]
fileHandle = open(fileName)
raw = fileHandle.readlines()

grid = []

def right(x, y):
    num = 0
    off = 0
    while y+off < col and grid[x][y+off].isdigit():
        num *= 10
        num += int(grid[x][y+off])
        off += 1
    return num

def left(x, y):
    num = ''
    off = 0
    while y-off > -1 and grid[x][y-off].isdigit():
        num = grid[x][y-off] + num
        off += 1
    return int(num)

def count(x, y):
    n = 0
    gear = []

    if grid[x][y+1].isdigit():
            n += 1
            gear.append(right(x,y+1))

    if grid[x][y-1].isdigit():
            n += 1
            gear.append(left(x,y-1))

    for i in [-1,1]:
        if grid[x-i][y] == '.':
            if grid[x-i][y+1].isdigit():
                n += 1
                gear.append(right(x-i,y+1))
            if grid[x-i][y-1].isdigit():
                n += 1
                gear.append(left(x-i,y-1))

        elif grid[x-i][y].isdigit():
            n += 1
            off = 1
            while y-off > -1 and grid[x-i][y-off].isdigit():
                off += 1
            gear.append(right(x-i, y-off+1))

    # print('n:', n, 'gear: ', gear )
    if n == 2:
        return gear[0] * gear[1]
    else:
        return 0
        
for x in raw:
    grid.append(x.strip('\n'))

row = len(grid) - 1
col = len(grid[1])
ans = 0

for x in range(row):
    for y in range(col):
        if grid[x][y] == '*':
            ans += count(x,y)
print(ans)


    