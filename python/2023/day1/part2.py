
fileName = 'input.txt'

fileHandle = open(fileName)
lines = fileHandle.readlines()

look = {
    'one': 1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9
}

values = 0
count = 1
found = False
for line in lines[:-1]:
    dis = len(line)
    val = []
    for n in range(dis - 1):
        if line[n] in look:
            val.append(look[line[n]])
            break
        if n + 6 > dis - 1:
            d = dis
        else:
            d = n + 6
        for x in range(n, d):
            # print(line[n:x])
            if line[n:x] in look:
                val.append(look[line[n:x]])
                found = True
                break
        if found:
            found = False
            break

    for n in range(dis - 1, -1, -1):
        if line[n] in look:
            val.append(look[line[n]])
            break
        if (n < (dis - 2)):  # when n is 9
            if n + 5 > dis - 1:
                d = dis
            else:
                d = n + 6
            for x in range(n + 3, d):
                if line[n:x] in look:
                    val.append(look[line[n:x]])
                    found = True
                    break
            if found:
                found = False
                break
    values += 10*val[0] + val[-1]
    print(count, 10*val[0] + val[-1])
    count += 1


print(values)


