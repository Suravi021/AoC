# yeah fuck youre life
fileName = 'test.txt'
fileHandle = open(fileName)

rows = [list(x.strip('\n')) for x in fileHandle.readlines()]
print(rows)
row_len = len(rows)
col_len = len(rows[0])

def render(matrix):
    print()
    n = len(matrix)
    m = len(matrix[0])
    for x in range(n):
        for y in range(m):
            print(matrix[x][y], end='')
        print()
    print()

def transpose(no_rows, no_cols,matrix):
    new = []
    for x in range(no_cols):
        temp = []
        for y in range(no_rows):
            temp.append(matrix[y][x])
        new.append(temp)
    return new


def colLeft(rows, cols, matrix):
    for x in range(rows):
        counter = 0
        square = 0
        for y in range(cols):
            z = matrix[x][y]
            if z == '#':
                square = y
                counter = 1
            elif z == 'O':
                savetime = counter + square
                matrix[x][savetime] = 'O'
                counter += 1
                if savetime != y:
                    matrix[x][y] = '.'
    return None

def colRight(rows, cols, matrix):
    for x in range(rows):
        counter = 0
        square = 0
        for y in range(cols):
            z = matrix[x][rows-y]
            if z == '#':
                square = rows-y
                counter = 1
            elif z == 'O':
                savetime = counter + square
                matrix[x][savetime] = 'O'
                counter += 1
                if savetime != y:
                    matrix[x][y] = '.'
    pass
r1 = transpose(row_len, col_len, rows)
colLeft(col_len, row_len, r1) # north but sleeping
rows = transpose(col_len, row_len, r1) # best position for west
colLeft(row_len, col_len, rows)
print('west done')
render(rows)
rows = rows[::-1]

r1 = transpose(row_len, col_len, rows)
colLeft(col_len, row_len, r1) # south but sleeping
rows = transpose(col_len, row_len, r1) # best position for east
render(rows)
rows = rows[::-1]
colRight(row_len, col_len, rows)
print('east done')
render(rows)


