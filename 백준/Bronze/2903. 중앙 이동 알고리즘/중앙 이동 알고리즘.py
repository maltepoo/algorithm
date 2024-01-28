n = int(input())
ns = [0]*16
ns[0] = 2

for i in range(1, n+1):
    ns[i] = ns[i-1]+(2**(i-1))

print(ns[n]**2)