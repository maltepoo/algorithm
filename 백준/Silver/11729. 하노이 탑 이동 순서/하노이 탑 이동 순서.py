"""
1. 첫 번째 재귀에서는 맨 밑의 N번째 원반을 목적지로 옮기기 위해 위의 N-1 개의 원반을 경유지로 옮긴다.
2. 그 다음 N 번째 원반을 목적지로 옮긴다.
3. 경유지에 있는 N-1 개의 원반을 to로 옮긴다.
https://shoark7.github.io/programming/algorithm/tower-of-hanoi
"""
n = int(input())
answer = 0
path = []

def move(st, ed):
    global answer
    answer += 1
    path.append("{} {}".format(st, ed))
    return


def hanoi(N, start, to, via):
    if N == 1:
        # 원반을 옮기고 종료
        move(start, to)
        return
    else:
        hanoi(N-1, start, via, to)
        move(start, to)
        hanoi(N-1, via, to, start)

hanoi(n, 1, 3, 2)
print(answer)
print(*path, sep="\n")
