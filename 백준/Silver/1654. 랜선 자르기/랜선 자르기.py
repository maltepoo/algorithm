k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
st, ed = 1, max(lan)

# 랜선 길이를 1 ~ 최대길이 사이에서 이분탐색으로 찾기
# 모든 랜선을 나눠보며 잘라진 개수가 n과 맞는것을 찾음
while st <= ed:
    mid = (st+ed)//2
    divided = 0
    for l in lan:
        divided += l//mid
    if divided >= n:
        st = mid+1
    else:
        ed = mid-1
print(ed)