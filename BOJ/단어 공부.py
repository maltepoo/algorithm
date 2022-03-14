s = input().upper()
alphas = [0]*26
for i in s:
    alphas[ord(i)-65] += 1
preq = []
for j in range(26):
    if alphas[j] == max(alphas):
        preq.append(chr(j+65))
print(*preq if len(preq) == 1 else '?')