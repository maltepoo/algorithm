def solution(number, k):
    res = []

    for n in number:
        while res and res[-1] < n and k > 0:
            res.pop()
            k -= 1
        res.append(n)

    if k > 0:
        res = res[:-k]
    return ''.join(res)