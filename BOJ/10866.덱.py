import sys
dq = []
def deque(cmd):
    global dq
    if cmd[0] == 'push_front':
        dq.insert(0, cmd[1])
    elif cmd[0] == 'push_back':
        dq.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if dq:
            print(dq.pop(0))
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if dq:
            print(dq.pop(-1))
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(dq))
    elif cmd[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if dq:
            print(dq[0])
        else: print(-1)
    elif cmd[0] == 'back':
        if dq:
            print(dq[-1])
        else: print(-1)
    return

n = int(input())
for _ in range(n):
    deque(sys.stdin.readline().split())