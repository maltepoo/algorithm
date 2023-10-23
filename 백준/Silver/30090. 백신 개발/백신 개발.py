def check(s1, s2):
    maxOverlap = min(len(s1), len(s2))
    for i in range(maxOverlap, 0, -1):
        if s1[-i:] == s2[:i]:
            return i, s1+s2[i:]
    return 0, s1+s2

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