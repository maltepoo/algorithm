n = int(input())
m = [int(str(n%10)+str((n//10+n%10)%10))]
while True:
    if m[-1] == n:
        print(len(m))
        break
    else:
        m.append(int(str(m[-1]%10)+str((m[-1]//10+m[-1]%10)%10)))