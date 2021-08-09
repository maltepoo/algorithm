#1936. 1대1 가위바위보
T = list(map(int, input().split()))
A = T[0]
B = T[1]

if A > B:
    print('A')
else:
    print('B')