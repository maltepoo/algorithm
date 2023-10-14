n, b = input().split()

res = 0
n = n[::-1]

# b진법 수 n을 10진법으로 바꾸기
for i, m in enumerate(n):
    if m.isalpha():
        m = ord(m)-65+10
    else:
        m = int(m)

    res += (int(b)**i)*m

print(res)