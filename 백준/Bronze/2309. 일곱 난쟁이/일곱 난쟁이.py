hobs = []
for _ in range(9):
    hobs.append(int(input()))
hobs.sort()
def findHobs():
    for i in range(9):
        ni = hobs[i]
        for j in range(9):
            nj = hobs[j]
            if i != j and sum(hobs)-(ni+nj) == 100:
                hobs.remove(ni)
                hobs.remove(nj)
                return
findHobs()
for h in hobs:
    print(h)