def solution(word):
    answer = 0
    alpha = ['A', 'E', 'I', 'O', 'U', ""]
    words = []
    for a in alpha:
        for b in alpha:
            for c in alpha:
                for d in alpha:
                    for e in alpha:
                        w = a+b+c+d+e
                        if not w in words: words.append(w)
    words.sort()
    answer = words.index(word)
    return answer