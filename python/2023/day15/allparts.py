fileName = 'input.txt'
fileHandle = open(fileName)

things = fileHandle.readline().strip('/n')
things = things.split(',')

ans = 0
def hashing(string):
    k = 0
    for t in string:
        k += ord(t)
        k *= 17
        k %= 256
    return k
def check(wtf, fuck, num):
    for x in wtf:
        if fuck == x[0]:
            x[-1] = num
            return None
    wtf.append([fuck,num])
    return None

def destroy(wtf, fuck):
    for x in wtf:
        if x[0] == fuck:
            wtf.remove(x)
            return None
    return None

for thing in things:
    ans += hashing(thing)
print('part1 ', ans)

labels = {}

#
# for thing in things:
#     if '=' in thing:
#         labels[thing[:-2]] = int(thing.split('=')[-1])
#
#     else:
#         labels[thing[:-1]] = 0
#
# for thing in things:
#     if '=' in thing:
#         m = thing[:-2]
#         print(m, hashing(m), end=' ')
#
#         print(int(thing.split('=')[-1]))
#     else:
#         m = thing[:-1]
#         print(m, hashing(m))

for thing in things:
    if '=' in thing:
        label = thing[:-2]
        focal = int(thing.split('=')[-1])
        box = hashing(label) + 1
        try:
            check(labels[box], label, focal)

        except KeyError:
            labels[box] = [[label, focal]]

    else:
        label = thing[:-1]
        box = hashing(label) + 1
        try:
            destroy(labels[box],label)
        except KeyError:
            continue

answer = 0

for x,f in labels.items():
    third = 1
    for f_sub in f:
        answer += (x * f_sub[-1] * third)
        third += 1
print('part2',answer)


