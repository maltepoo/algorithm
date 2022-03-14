n, x = map(int, input().split())
ns = list(map(int, input().split()))
for i in ns:
    if x > i:
        print(i, end=" ")