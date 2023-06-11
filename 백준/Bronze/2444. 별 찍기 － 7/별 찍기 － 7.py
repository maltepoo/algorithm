n = int(input())
for i in range(1, n*2, 2):
    print(' '*(n-(i//2+1)) + '*'*i)
for j in range(n*2-3, 0, -2):
    print(' '*(n-(j//2+1)) + '*'*j)