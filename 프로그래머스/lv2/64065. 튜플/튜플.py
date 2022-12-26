def solution(s):
    answer = []
    s = sorted(map(lambda x: x.replace("{", "").replace('}', ""), s.split("},{")), key=lambda x: len(x))
    for tuples in s:
        tuples = list(map(int, tuples.split(",")))
        for t in tuples:
            if not t in answer:
                answer.append(t)
    return answer