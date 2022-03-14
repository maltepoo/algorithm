hour, min = map(int, input().split())
time = int(input())
if time+min >= 60:
    hour += (time+min)//60
    if hour >= 24:
        print(hour%24, (time+min) % 60)
    else:
        print(hour, (time+min) % 60)
else:
    print(hour, time+min)