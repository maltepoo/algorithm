n, b = map(int, input().split())
answer = ""

while n:
    d = n%b
    if d >= 10:
        d += 55
        answer += chr(d)
    else:
        answer += str(d)
    n //= b

print(answer[::-1])