n = int(input())
res = 0
total = 0
st, ed = 0, 0

while ed <= n: #ed가 n보다 커지면 수 범위를 넘은 것
    if total == n:
        res += 1
        ed += 1
        total += ed
    elif total < n: #총합이 수보다 작으면 큰수를 더해본다
        ed += 1
        total += ed
    elif total > n: #총합이 수보다 크면 작은수를 올려 범위를 좁힌다
        total -= st
        st += 1
print(res)