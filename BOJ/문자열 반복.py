s = int(input())
for i in range(s):
    n, string = map(str, input().split())
    for i in string:
        print(i*int(n),end="")
    print()