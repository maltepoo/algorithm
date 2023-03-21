n, m = map(int, input().split()) #큐의 크기, 뽑는 수의 개수
loc = list(map(int, input().split())) #뽑아내려는 수의 위치들

cnt = 0
q = [i for i in range(1, n+1)]

def q_left():
    first = q.pop(0)
    q.append(first)

def q_right():
    last = q.pop()
    q.insert(0, last)

for l in loc:
    while True:
        if q[0] == l: #현재가 뽑으려는 숫자면 뽑고 종료
            q.pop(0)
            break
        else:
            if q.index(l) <= len(q)//2: #목표요소의 현재위치(0)와의 거리차이가 q길이 절반 이하인쪽으로
                q_left()
                cnt += 1
            else:
                q_right()
                cnt += 1
print(cnt)