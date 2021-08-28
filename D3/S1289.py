#1289. 원재의 메모리 복구하기
T = int(input())
for tc in range(1, T+1):
    mm = input()

    cnt = 0
    for i in range(len(mm)-1):
        if mm[i] != mm[i+1]:
            cnt += 1
    if mm[0] == '1':
        cnt += 1
    print('#{} {}'.format(tc, cnt))