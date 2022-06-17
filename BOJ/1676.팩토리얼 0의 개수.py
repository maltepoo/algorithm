"""
뒷자리가 0이 나오는 경우는 2, 5, 10을 곱했을 때이며
5를 곱하면 몇개의 0이 나오는지 알 수 있다
"""
n = int(input())
cnt = 0
while n >= 5:
    cnt += n // 5
    n //= 5
print(cnt)