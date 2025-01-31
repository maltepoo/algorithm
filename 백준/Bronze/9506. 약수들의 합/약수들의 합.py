# 9506 n이 완전수인지 판별
def find_nums(n):
    # n을 제외한 약수들을 반환
    # n의 제곱근까지 나누면 약수
    m = set()
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i) == 0:
            m.add(i)
            if (i ** 2) != n:
                m.add(n // i)
    return sorted(m)[:-1]


def is_pefrect(n):
    nums = find_nums(n)
    if n == sum(nums):
        return True, nums
    return False, nums


while True:
    n = int(input())
    if n == -1: break
    
    perfect, nums = is_pefrect(n)
    if perfect:
        print(f'{n} = ', end='')
        print(*nums, sep=' + ')
    else:
        print(f'{n} is NOT perfect.')