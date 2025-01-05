# 1629 a를 b번 곱한 수를 c로 나눈 나머지 출력

def dac(n, i, j):
    if i == 1:
        return n % j
    elif i % 2 == 0:
        return (dac(n, i//2, j)**2)%j
    return ((dac(n, i//2, j)**2)*n)%j # b가 홀수일경우

a, b, c = map(int, input().split())
print(dac(a, b, c))