fileName = 'input.txt'

fileHandle = open(fileName)
lines = fileHandle.readlines()

values = 0

for line in lines[:-1]:
    val = []
    for num in line:
        k = ord(num)
        if k > 47 and k < 58:
            val.append(int(num))
    values += 10*val[0] + val[-1]

print(values)


