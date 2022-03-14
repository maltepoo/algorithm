a, b, c = int(input()), int(input()), int(input())
num = [0]*10
for i in str(a*b*c):
    num[int(i)] += 1
print(*num,sep="\n")