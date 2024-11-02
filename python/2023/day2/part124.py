fileName = "input.txt"
fileHandle = open(fileName)

games = fileHandle.readlines()

ans = 0

for game in games:
    red, green, blue = 0, 0, 0
    game = game.strip('\n')
    part1, part2 = game.split(':')
    add = True
    for x in part2.split(';'):
        add = True
        for y in x.split(','):
            if y[-1] == 'd':
                if int(y[1:-4]) > red:
                    red = int(y[1:-4])
            elif y[-1] == 'n':
                if int(y[1:-6]) > green:
                    green = int(y[1:-6])
            else:
                if int(y[1:-5]) > blue:
                    blue = int(y[1:-5])
    ans += red * blue * green
print("part2:", ans)



