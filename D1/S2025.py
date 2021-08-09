#2025. N줄덧셈
T = int(input())
res = 0

for i in range(0, T):
    i += 1
    res = i + res
    if res == 10000:
        break
print(res)