n, m = map(int, input().split(" "))
ant1 = list(zip(list(input()), [1]*n))
ant2 = list(zip(list(input()), [2]*m))
t = int(input())

match = ant1[::-1]+ant2
change = []
for sc in range(t):
    for i in range((n+m)-1):
        if match[i][1] == 1 and match[i+1][1] == 2:
            change.append(i)
    while change:
        target = change.pop()
        match[target], match[target+1] = match[target+1], match[target]
print("".join([a for a, b in match]))