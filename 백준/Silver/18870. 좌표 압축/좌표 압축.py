import sys
input = sys.stdin.readline

n = int(input())
xs = list(map(int, input().split()))
loc_dict = {}

loc = sorted(set(xs))
for l in range(len(loc)):
    loc_dict[loc[l]] = l

for i in xs:
    print(loc_dict[i], end=" ")