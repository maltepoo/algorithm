n = int(input())
k = int(input())


# 답 범위는 1 <= res <= k
# 인덱스 k보다 큰 수가 k위치에 올 수 없기 때문
# 임의의 x값을 설정하고 x보다 작거나 같은 원소의 개수가 k 값이랑 일치하면 정답
# x = 3일때, 3보다 작은 수가 5개라면 B[5]는 3이라는 소리가 된다
def binary_search(start, end):
    while start <= end:
        m = (start+end)//2

        cnt = 0
        for i in range(1, n+1):
            # i(행)으로 m(답 예상수), k보다 작은 수가 몇 개인지 체크
            cnt += min(m//i, n)

        # k보다 작은 수의 개수가 k보다 크면 더이상 탐색할 필요 없음
        if cnt >= k:
            end = m-1
        else:
            start = m+1
    return start
print(binary_search(1, k))
