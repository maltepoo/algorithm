L = int(input())
string = list(input())
res = 0
for i in range(len(string)):
    res += (ord(string[i])-96)*(31**i)
print(res%1234567891)
