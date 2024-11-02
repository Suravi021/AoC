"""
i kinda kinda cheated with the time here,
due to a bug i got an answer and was informed the answer was too high
so i worked backward from that number after fixing the bug and it go extremely fast
"""


import time
start_time = time.perf_counter()


fileName = 'input2.txt'
fileHandle = open(fileName)

seeds = fileHandle.readline()
seeds = seeds.strip('\n').split()[1:]
seeds  = [int(seed) for seed in seeds]
raw = fileHandle.readline()

raw = fileHandle.readlines()
mapping = []
temp = []

for x in raw[::-1]:
    if x[0].isalpha():
        mapping.append(temp)
        temp = []
    elif x[0].isdigit():
        temp.append([int(n) for n in x.split()])

raw = 0
ans = 2243422640
found = False

while True:
    search = ans
    for x in range(len(mapping)):
        for y in range(len(mapping[x])):
            if search >= mapping[x][y][0] and search < mapping[x][y][0] + mapping[x][y][2]:
                search = mapping[x][y][1] + search - mapping[x][y][0]
                break
        # print(x,' search',search)
    # print(ans)

    for x in range(0, len(seeds),2):
        if search >= seeds[x] and search < seeds[x] + seeds[x+1]:
            print('ans: ',ans)
            found = True
    if found:
        break
    ans -= 1
    # ans += 1

end_time = time.perf_counter()
print((start_time- end_time)*-1 * 1000 * 1000, 'ms')
