'''
6.    five of a kind - 1 
5.    4 of kind - 2
4.    3, 2 of a kind - 2
3.    three of a kind - 3
2.    2 of a pair - 3
1.    one pair - 4
0.    all diff - 5

'''

import sys


def category(card):
    d = {}
    for x in card:
        try:
            d[x] += 1
        except:
             d[x] = 1
        
    length = len(d)
    if 'J' in card:
        if length == 5:
            #all are diff
            return 1
        
        elif length == 4:
            return 3
        
        elif length == 3:
            for x in d.values():
                if x == 3:
                    return 5
            if d['J'] == 2:
                return 5
            return 4

        elif length == 2 or length == 1:
            return 6
    else:
        if length == 1:
            return 6
        elif length == 5:
            return 0
        elif length == 4:
            return 1
        elif length == 3:
            for x in d.values():
                if x == 3:
                    return 3
            return 2
        else:
            for x in d.values():
                if x == 4:
                    return 5
            return 4

def category2(card):
    d = {}
    for x in card:
        try:
            d[x] += 1
        except:
            d[x] = 1
    
    try:
        d.pop('J')
    except:
        pass
    
    length = len(d)
    print(length)
    if length == 1:
        return 6
    elif length == 5:
        return 0
    elif length == 4:
        return 1
    elif length == 3:
        for x in d.values():
            if x == 3:
                return 3
        return 2
    else:
        for x in d.values():
            if x == 4:
                return 5
        return 4

def compare(x, y):
    n = 0
    while n < 5:
        if(x[n] != y[n]):
            break
        n += 1
    if standards[x[n]] > standards[y[n]]:
        return True
    return False
        


fileName = sys.argv[1]
fileHandle = open(fileName)

bets = {}
allCards = []
standards = {
    'J': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5, 
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 12,
    'K': 13,
    'A': 14
}


for _ in range(7):
    allCards.append([])

for x in fileHandle.readlines():
    k, v = x.strip('\n').split()
    bets[k] = int(v)
    allCards[category(k)].append(k)


print(allCards)

for i in range(7):
    length = len(allCards[i])
    for x in range(length):
        for y in range(length - 1 - x):
            if compare(allCards[i][y], allCards[i][y+1]):
                allCards[i][y], allCards[i][y+1] = allCards[i][y+1], allCards[i][y]

n = 1
ans = 0

for i in range(7):
    for j in range(len(allCards[i])):
        ans += bets[allCards[i][j]] * n
        n += 1

print(ans)


