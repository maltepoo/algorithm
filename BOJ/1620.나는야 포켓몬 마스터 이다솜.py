import sys
n, m = map(int, sys.stdin.readline().split())
book = {}
book_reversed = {}
for i in range(1, n+1):
    ipt = sys.stdin.readline().strip()
    book[i] = ipt
    book_reversed[ipt] = i
for j in range(m):
    target = sys.stdin.readline().strip()
    if target.isnumeric():
        print(book[int(target)])
    else:
        print(book_reversed[target])