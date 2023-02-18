def factorial(m):
    ans = 1
    for i in range(2, m+1):
        ans *= i
    return ans

n, k = map(int, input().split(" "))
print(factorial(n) // factorial(k) // factorial(n-k))