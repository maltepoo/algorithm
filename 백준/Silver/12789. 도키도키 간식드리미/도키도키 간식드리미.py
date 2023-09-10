n = int(input())
wait = list(map(int, input().split()))[::-1]
space = []

m = 1
while wait:
    w = wait.pop()
    if w == m:
        m += 1
    else:
        space.append(w)
    while space:
        if space[-1] == m:
            space.pop()
            m += 1
        else:
            break
print("Sad" if space else "Nice")