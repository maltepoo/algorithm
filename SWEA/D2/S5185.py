#5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수
T = int(input())
for tc in range(1, T+1):
    N, n16 = input().split()
    print('#{} {}'.format(tc, bin(int(n16,16))[2:].zfill(int(N)*4)))