from itertools import permutations

def isPrime(n):
    for i in range(2, int(n**0.5)+1): # 제곱근까지의 숫자로 나누어 판별
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    able = list(numbers)
    for i in range(1, len(numbers)+1):
        for n in permutations(numbers, i):
            able.append("".join(n))
    able = list(map(int, set(able)))
    for a in set(able):
        if int(a) < 2: continue
        if isPrime(int(a)):
            answer += 1
    return answer