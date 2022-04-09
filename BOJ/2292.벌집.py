n = int(input())
honeyComb, cnt = 1, 1
while n > honeyComb:
    honeyComb += cnt * 6
    cnt += 1
print(cnt)