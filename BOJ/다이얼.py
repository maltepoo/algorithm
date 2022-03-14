s = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
res = 0
for i in s:
    for j in range(8):
        if i in dial[j]:
            res += j+3
print(res)