n, k = map(int, input().split())
몇번째 = 0
체크 = False
for i in range(1, n+1):
    if n%i == 0:
        몇번째 += 1
    if 몇번째 == k:
        print(i)
        체크 = True
        break
if not 체크:
    print(0)