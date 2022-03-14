n, m = 0, 0
for i in range(1, 10):
    ipt = int(input())
    if ipt > n:
        n = ipt
        m = i
print(n, m, sep='\n')
