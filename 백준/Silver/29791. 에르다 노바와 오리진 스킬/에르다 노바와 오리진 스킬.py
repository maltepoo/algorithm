def check_affected_skill_cnt(lst, type):
    cnt, time = 0, 0
    cool = 100 if type == "E" else 360
    for i in lst:
        if time <= i:
            time = (i+cool)
            cnt += 1
    return cnt

e, o = map(int, input().split())
erdaT = sorted(map(int, input().split()))
orgnT = sorted(map(int, input().split()))

print(check_affected_skill_cnt(erdaT, "E"), check_affected_skill_cnt(orgnT, "O"))