def solution(n, words):
    answer = [0,0]
    usedWords = [words[0]]

    for i in range(1, len(words)):
        order = (i%n)+1
        number = (i//n)+1
        
        a, b = words[i-1], words[i]
        if a[-1] != b[0] or words[i] in usedWords:
            answer = [order, number]
            break
            
        usedWords.append(words[i])
        
    return answer