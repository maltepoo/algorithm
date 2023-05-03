# n의 범위가 4*10^9이기 때문에 에라토스테네스의 체는 사용불가
def isPrime(m):
    if m == 0 or m == 1: # 0, 1은 합성수, 소수 아님
        return False
    for i in range(2, int(m**0.5)+1): # 제곱 근까지 나눠 소수판별
        if m % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    while True:
        if isPrime(n):
            print(n)
            break
        else:
            n += 1