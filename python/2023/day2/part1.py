    # Game 100: 8 red, 3 green; 4 green, 1 blue, 15 red; 10 red, 8 green, 1 blue

fileName = 'input.txt'
fileHandle = open(fileName)
lines = fileHandle.readlines()
gameIds = 0
n = 0
for line in lines[:-1]:
    add = True
    final = []
    n += 1
    for x in line.split(':')[-1].split(';'):
        balls = x.split(',')
        for m in balls:
            ball = m.split()
            final += ball
    for k in range(0,len(final),2):
        if int(final[k]) > 12 and final[k+1] == 'red':
            add = False
            break
        elif int(final[k]) > 14 and final[k+1] == 'blue':
            add = False
            break
        elif int(final[k]) > 13 and final[k+1] == 'green':
            add = False
            break
    if add:
        gameIds += n

print(gameIds)




