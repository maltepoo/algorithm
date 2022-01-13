#3499. 퍼펙트 셔플
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    word = input().split()

    mid = len(word) // 2
    res = []
    idx = 1
    while idx < mid:
        if len(word) % 2 == 0:
            for i in range(mid):
                try:
                    res.append(word[i])
                    res.append(word[i+mid])
                    idx += 1
                except:
                    pass

        else:
            for i in range(mid+1):
                try:
                    res.append(word[i])
                    res.append(word[i + mid+1])
                    idx += 1
                except:
                    pass
    print('#{} '.format(tc), end="")
    print(*res)