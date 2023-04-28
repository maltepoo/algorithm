m = int(input())
n = int(input())
primes = []

def isPrime(num):
    if num == 0 or num == 1:
        return False
    for p in range(2, num):
        if num % p == 0:
            return False
    return True

for i in range(m, n+1):
    if isPrime(i):
        primes.append(i)

if primes:
    print(sum(primes))
    print(min(primes))
else: print(-1)