fileName = 'input.txt'
fileHandle = open(fileName)

seeds = fileHandle.readline()[:-1].split()[1:]
seeds = [int(x) for x in seeds]

lines = fileHandle.readlines()
lines = lines[1:-1]
lines = [x[:-1] for x in lines]

while True:
    try:
        lines.remove('')
    except ValueError:
        break
print(lines)
seeds_copy = seeds[:]
for x in lines:
    try:
        temp = [int(m) for m in x.split()]
        for seed in zip(seeds,range(len(seeds))):
            if (seed[0] >= temp[1]) and (seed[0] < (temp[1] + temp[2])):
                seeds_copy[seed[1]] = temp[0] + seed[0] - temp[1]

    except ValueError:
        seeds = seeds_copy[:]
        print(seeds_copy)
        continue


print(seeds_copy)
seeds_copy.sort()
print(seeds_copy[0])
