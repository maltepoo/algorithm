n = int(input())
numbers = list(map(int, input().split(" ")))
p, mn, mu, dv = map(int, input().split(" "))  # 덧셈,뺄셈,곱셈,나눗셈
min_value = int(1e9)
max_value = -int(1e9)


def dfs(v, d, p, mn, mu, dv):
    global min_value, max_value
    if d == n:
        min_value = min(v, min_value)
        max_value = max(v, max_value)
        return

    if p > 0:
        dfs(v + numbers[d], d + 1, p - 1, mn, mu, dv)
    if mn > 0:
        dfs(v - numbers[d], d + 1, p, mn - 1, mu, dv)
    if mu > 0:
        dfs(v * numbers[d], d + 1, p, mn, mu - 1, dv)
    if dv > 0:
        dfs(int(v / numbers[d]), d + 1, p, mn, mu, dv - 1)


dfs(numbers[0], 1, p, mn, mu, dv)
print(max_value)
print(min_value)