def solution(n, words):
    answer = [0,0] # person, round
    before = []
    r = 1
    for i in range(0, len(words), n):
        for j in range(n):
            if r == 1:
                before.append(words[i+j])
            else:
                if words[i+j-1][-1] != words[i+j][0] or words[i+j] in before or len(words[i+j])<2:
                    answer[0] = j+1
                    answer[1] = r
                    return answer
                else:
                    before.append(words[i+j])
        r += 1
    return answer
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "e", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))