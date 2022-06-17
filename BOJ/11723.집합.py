import sys
s = set()
m = int(sys.stdin.readline())

for _ in range(m):
    tmp = sys.stdin.readline().split()
    if len(tmp) == 1:
        if tmp[0] == "all":
            s = set([i for i in range(1, 21)])
        elif tmp[0] == "empty":
            s = set()
    else:
        cmd, n = tmp[0], int(tmp[1])
        if cmd == "add":
            s.add(n)
        elif cmd == "remove":
            s.discard(n)
        elif cmd == "check":
            if n in s: print(1)
            else: print(0)
        elif cmd == "toggle":
            if n in s: s.discard(n)
            else: s.add(n)