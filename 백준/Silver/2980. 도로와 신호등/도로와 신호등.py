n, l = map(int, input().split(" "))
lights = []
loc, second = 0, 0 #현재위치, 총 초수
for _ in range(n):
    d, r, g = map(int, input().split(" "))
    second += (d-loc)
    loc = d
    if second % (r+g) < r: #빨간불이면
        second += (r - second % (r+g)) #초록불이 될때까지 기다리기
second += l-loc #마지막 지점에서 도로끝까지
print(second)