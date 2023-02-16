from collections import deque

n, l = map(int, input().split())
a = list(map(int, input().split()))

window = deque()
for i in range(n):
    while window and window[0][1] <= i-l: #i-l 범위를 넘으면 삭제
        window.popleft()
    while window and window[-1][0] > a[i]: #들어올 원소(a[i])보다 현재 덱에 있는게 크면 삭제
        window.pop()
    window.append((a[i], i)) #원소추가
    print(window[0][0], end = " ") #매번 맨 앞에 있는 값이 최소가 되므로 그냥 출력