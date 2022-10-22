def solution(n, words):
    answer = [0,0] # person, round
    before = [words[0]]
    for i in range(0, len(words), n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if words[i+j-1][-1] != words[i+j][0] or words[i+j] in before or len(words[i+j])<2:
                answer[0] = j+1
                answer[1] = ((i+j) // n)+1
                return answer
            else:
                before.append(words[i+j])
    return answer
print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))

"""
1차 풀이
def solution(n, words):
    answer = [0,0] # person, round
    before = []
    for i in range(0, len(words), n):
        r = i+1 # round
        for j in range(n):
            if r == 1:
                if j == 0:
                    before.append(words[i+j])
                else:
                    if words[i+j-1][-1] != words[i+j][0] or words[i+j] in before or len(words[i+j])<2:
                        answer[0] = j+1
                        answer[1] = (r // n)+1
                        return answer
                    else:
                        before.append(words[i+j])
            else:
                if words[i+j-1][-1] != words[i+j][0] or words[i+j] in before or len(words[i+j])<2:
                    answer[0] = j+1
                    answer[1] = (r // n)+1
"""