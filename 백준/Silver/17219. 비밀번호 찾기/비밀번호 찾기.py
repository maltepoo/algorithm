import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sites = {}
for _ in range(n):
    s, p = input().split()
    sites[s] = p
for _ in range(m):
    url = input().strip()
    print(sites[url])