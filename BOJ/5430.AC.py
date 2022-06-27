import sys
t = int(sys.stdin.readline())
for _ in range(t):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().rstrip()[1:-1].split(',')
    flag = False
    err = False
    if n == 0:
        arr = []
    for od in p:
        if od == 'R':
            flag = not flag
        elif od == 'D':
            if len(arr) == 0:
                err = True
                break
            else:
                if flag:
                    arr.pop()
                else:
                    arr.pop(0)
    if err:
        print('error')
    else:
        if flag:
            arr.reverse()
        print('[', end="")
        print(','.join(arr), end="")
        print(']')