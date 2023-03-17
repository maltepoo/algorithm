from itertools import permutations
a, b = input().split()
perm = list(map(lambda x: ("".join(x)), sorted(permutations(list(a), len(a)), reverse=True)))
maxV = -1
for p in perm:
    p = int(p)
    if len(str(p)) != len(a):
        continue
    if p < int(b) and maxV < p:
        maxV = p
print(maxV)