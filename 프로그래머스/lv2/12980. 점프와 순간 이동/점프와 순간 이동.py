def solution(n):
    ans = 1
    while n > 2:
        if n % 2 == 0:
            n /= 2
        else:
            ans += 1
            n -= 1
    return ans
# 순간이동을 하려면 무조건 1칸을 가야 해서 ans = 1로 시작
# 2로 나누어지면 순간이동, 안되면 움직이므로 +1
"""
bottom-up (시간초과)
def solution(n):
    arr = [0 for _ in range(n+1)]
    arr[1], arr[2] = 1, 1
    
    for i in range(3, n+1):
        if i%2 == 0:
            arr[i] = arr[i//2]
        else:
            arr[i] = arr[i//2]+1
    return arr[-1]
"""