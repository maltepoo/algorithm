n, m = map(int, input().split())
bulbs = list(map(int, input().split()))
cmd = [list(map(int, input().split())) for _ in range(m)]

def toggle_bulb(idx):
    if bulbs[idx] == 1:
        bulbs[idx] = 0
    else: bulbs[idx] = 1
    return

for i in range(m):
    a, r, l = cmd[i][0], cmd[i][1]-1, cmd[i][2]
    if a == 1:
        bulbs[r] = cmd[i][2]
    elif a == 2:
        for j in range(r, l):
            toggle_bulb(j)
    elif a == 3:
        for j in range(r, l):
            bulbs[j] = 0
    else:
        for j in range(r,l):
            bulbs[j] = 1
print(*bulbs)