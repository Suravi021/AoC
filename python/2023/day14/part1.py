fileName = 'input.txt'
fileHandle = open(fileName)

rows = [x.strip('\n') for x in fileHandle.readlines()]

new =[]
no_rows = len(rows)
no_cols = len(rows[0])

linked = {}
for c in range(1, no_rows + 1):
    linked[c] = 0

for col in range(no_cols):
    d = no_rows
    for row in range(no_rows):
        if rows[row][col] == 'O':
            linked[d] += 1
        elif rows[row][col] == '.':
            continue
        else:

            d = no_rows - row
            if d == 1:
                break
        d -= 1

print(linked)

ans = 0

for value in linked.keys():
    ans += value * linked[value]

print(ans)