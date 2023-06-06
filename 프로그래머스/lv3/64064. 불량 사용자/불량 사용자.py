answer = set()


def comf(a, b):
    n = len(a)
    for i in range(n):
        if a[i] != b[i] and b[i] != '*':
            return False
    return True


def solution(user_id, banned_id):
    banned = {}
    for i in range(len(banned_id)):
        banned[i] = []

    for user in user_id:
        for bi in range(len(banned_id)):
            if len(user) == len(banned_id[bi]) and comf(user, banned_id[bi]):
                banned[bi].append(user)

    vals = list(banned.values())

    def dfs(d, arr):
        global answer
        if d == len(banned_id):
            answer.add(tuple(sorted(arr)))
            return
        for val in vals[d]:
            if not val in arr:
                arr.append(val)
                dfs(d + 1, arr)
                arr.pop()
        return

    dfs(0, [])
    return len(answer)