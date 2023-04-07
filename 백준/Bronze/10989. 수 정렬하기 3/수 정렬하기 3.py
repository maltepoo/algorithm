# 카운팅 정렬 사용문제
# 메모리제한이 작아 배열을 저장할 수 없고 입력값의 범위가 커 입력값을 바로 배열의 인덱스로 사용할 수 없음
import sys
input = sys.stdin.readline
n = int(input())
cnt = [0]*10001
for i in range(n):
    cnt[int(input())] += 1

for j in range(1, 10001):
    if cnt[j] != 0:
        # cnt[j]의 개수만큼 j를 출력
        for k in range(cnt[j]):
            print(j)