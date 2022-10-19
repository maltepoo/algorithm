def solution(skill, skill_trees):
    answer = 0

    for st in skill_trees:
        idx, flag = 0, True
        for i in range(len(st)):
            if not st[i] in skill:
                continue
            else:
                if st[i] != skill[idx]:
                    flag = False
                else:
                    idx += 1
        if flag: answer += 1
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))