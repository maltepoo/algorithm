def changeNumber(n, k):
    res = ""
    while 0 < n:
        res = str(n % k) + res
        n //= k
    return res

def isPrime(n):
    if n == 1: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    res = changeNumber(n, k)
    temp = ""
    for i in range(len(res)):
        if res[i] != '0':
            temp += res[i]
        else:
            if temp != "" and isPrime(int(temp)):
                answer += 1
            temp = ""
    if temp != "" and isPrime(int(temp)):
        answer += 1
    return answer

print(solution(437674, 3))
print(solution(110011, 10))