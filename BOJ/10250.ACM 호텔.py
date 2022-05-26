t = int(input())
for _ in range(t):
    h,w,n = map(int, input().split())
    floor = (n % h) if (n % h) > 0 else h
    room = (n // h) if (n % h) == 0 else (n // h)+1
    print(str(floor)+("0"+str(room) if room < 10 else str(room)))