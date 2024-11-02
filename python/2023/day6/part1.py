time = [71530]
distance = [940200]

ans = 1
temp = 0
for t,d in zip(time, distance):
    for x in range(t):
        if ((t-x)*x) > d:
            temp += 1
    ans *= temp
    temp = 0

print(ans)
