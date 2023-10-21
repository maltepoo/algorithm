def check(s1, s2):
    cnt, j = 0, 0
    if s2 in s1:
        return len(s2), s1
    for i in range(len(s1)):
        if s1[i] == s2[j] and j < len(s2)-1:
            cnt += 1
            j += 1
    return cnt, s1+s2[cnt:]

def find_vaccine(s, visited, d):
    global maxword
    if d == len(word):
        maxword = min(maxword, len(s))
        return maxword

    for w in word:
        if not w in visited:
            overlap, newstr = check(s, w)
            if len(newstr) < maxword:
                visited.append(w)
                find_vaccine(newstr, visited, d + 1)
                visited.pop()

n = int(input())
word = sorted(set([input() for _ in range(n)]))
maxword = sum(map(lambda x: len(x), word))

for w in word:
    find_vaccine(w, [w], 1)

print(maxword)