def isPassedDate(base_date, target_date):
    for i in range(3):
        if target_date[i] < base_date[i]:
            return True
        elif target_date[i] > base_date[i]:
            return False
    return False

def solution(today, terms, privacies):
    answer = []
    today = list(map(int, today.split(".")))

    terms_dict = {}
    for t in terms:
        name, month = t.split(" ")
        terms_dict[name] = int(month)
        
    for p in range(len(privacies)):
        start, term = privacies[p].split(" ")
        start = list(map(int, start.split(".")))
        expire = [start[0], start[1] + terms_dict[term], start[2]-1]

        if expire[2] > 28:
            expire[1] = expire[2] // 28
            expire[2] = expire[2] % 28
        if expire[1] > 12:
            expire[0] = expire[0] + expire[1] // 12
            expire[1] = expire[1] % 12
        if expire[1] == 0:
            expire[1] = 12
            expire[0] = expire[0] - 1
        if expire[2] == 0:
            expire[2] = 28
            expire[1] = expire[1] - 1

        if isPassedDate(today, expire):
            answer.append(p+1)
    return answer