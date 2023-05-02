s = list(input())
t = list(input())

ans = 0
# 방법1: 문자열의 뒤에 A를 추가
# 방법2: 문자열을 뒤집고 뒤에 B 추가
while len(t) > len(s):
    if t[-1] == 'A':
        t.pop()
    else:
        t.pop()
        t = t[::-1]
    if s == t:
        ans = 1
        break
print(ans)