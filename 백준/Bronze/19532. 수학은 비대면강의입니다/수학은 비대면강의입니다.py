a, b, c, d, e, f = map(int, input().split())

def solve(x, y):
    if a*x + b*y == c and d*x+e*y == f:
        return True
    return False

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if solve(i, j):
            print(i, j)
            break