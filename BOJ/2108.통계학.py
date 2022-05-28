n = int(input())
ns = [int(input()) for _ in range(n)]
print(round(sum(ns)/n), sorted(ns)[n//2], sep="\n")
counter = {}
for i in range(n):
    if counter.get(ns[i]) is None:
        counter[ns[i]] = 1
    else:
        counter[ns[i]] += 1
res = []
mv = max(counter.values())
for j in counter:
    if counter[j] == mv:
        res.append(j)
res.sort()
if len(res) > 1:
    print(res[1])
else: print(res[0])
print(max(ns)-min(ns))
