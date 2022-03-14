def factorial(n, res=1):
    if n <= 1:
        return res
    return factorial(n-1, res*n)
print(factorial(int(input())))