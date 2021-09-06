#2007. 패턴 마디의 길이
def isPattern(words, w):
    lg = len(w)
    if w == words[lg:lg*2] and w == words[lg*2:lg*2+lg]:
        return True

T = int(input())
for tc in range(1, T+1):
    words = input()
    res = 0
    for i in range(1, 30):
        w = words[0:i]
        if isPattern(words, w):
            res = len(w)
            break

    print('#{} {}'.format(tc, res))