def d(n):
    res = n
    for i in str(n):
        res += int(i)
    return res

non = []
for i in range(1, 10001):
    non.append(d(i))
for j in range(1, 10001):
    if not j in non:
        print(j)