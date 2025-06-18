n = int(input())
MOD = 9901

a, b, c = 1, 1, 1  # 이전 열의 0, 1, 2 상태

for _ in range(2, n+1):
    a_new = (a + b + c) % MOD
    b_new = (a + c) % MOD
    c_new = (a + b) % MOD
    a, b, c = a_new, b_new, c_new

print((a + b + c) % MOD)