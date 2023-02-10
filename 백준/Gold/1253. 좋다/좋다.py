n = int(input())
nums = sorted(map(int, input().split(" ")))

def findCombiNums(idx, target):
    li = nums[:idx]+nums[idx+1:]
    fr, to = 0, len(li)-1
    while fr < to:
        t = li[fr]+li[to]
        if t == target:
            return True
        if t < target:
            fr += 1
        else:
            to -= 1
    return False

cnt = 0
for i in range(n):
    if findCombiNums(i, nums[i]):
        cnt += 1
print(cnt)