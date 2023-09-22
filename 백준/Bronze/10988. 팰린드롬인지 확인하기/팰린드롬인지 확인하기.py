w = input()

size = len(w)-1
n = size // 2

answer = 1

i, j = 0, size
while i <= n <= j:
    if w[i] != w[j]:
        answer = 0
        break
    i += 1
    j -= 1

print(answer)