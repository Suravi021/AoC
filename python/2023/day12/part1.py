def count():
    
    
    return val






FileName = 'input.txt'
ans = 0
FileHandle = open(FileName)

lines = FileHandle.readlines()

for line in lines:
    line = line.strip('\n')
    cfg, num = line.split()
    num = tuple(map(int,num.split(',')))
    ans += count()

    print(ans)

    