n = int(input())
nums = list(map(int, input().split(" ")))

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
cnt = 0
for m in nums:
    if isPrime(m):
        cnt += 1
print(cnt)