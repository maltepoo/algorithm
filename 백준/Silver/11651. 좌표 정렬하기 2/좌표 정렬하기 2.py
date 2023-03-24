import sys
input = sys.stdin.readline
n = int(input())
numbers = [list(map(int, input().split())) for _ in range(n)]

numbers.sort(key=lambda x: (x[1], x[0]))
for n in numbers:
    print(*n)