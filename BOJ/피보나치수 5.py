# 재귀
n = int(input())
def fibo(m):
    if m <= 1:
         return m
    else:
        return fibo(m-1) + fibo(m-2)
print(fibo(n))

# 반복문
n = int(input())
fibo = [0, 1]
for i in range(n-1):
    fibo.append(fibo[-1]+fibo[-2])
print(fibo[n])