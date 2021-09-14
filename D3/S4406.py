#4406. 모음이 보이지 않는 사람
T = int(input())
for tc in range(1, T+1):
    word = list(input())
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = ''
    for w in word:
        if w not in vowels:
            res += w
    print('#{} {}'.format(tc, res))