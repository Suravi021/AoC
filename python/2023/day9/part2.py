fileName = 'input.txt'

def process(s):
    s = s.split()
    s = [int(x) for x in s]
    return s
def zeroes(check):
    for x in check:
        if x != 0:
            return False
    return True

def predict(s):
    all = []
    all.append(s)
    while True:
        one = []
        for x in range(1,len(s)):
            one.append(s[x]-s[x-1])
        if zeroes(one):
            break
        all.append(one)
        s = one[:]

    while True:
        try:
            all[-2].insert(0,all[-2][0]-all[-1][0])
            all = all[:-1]
        except IndexError:
            break
    return all[0][0]

answer = 0

fileHandle = open(fileName)

while True:
    x = fileHandle.readline().strip('\n')
    if x != '':
        x = process(x)

        answer +=  predict(x)
    else:
        break
print(answer)
