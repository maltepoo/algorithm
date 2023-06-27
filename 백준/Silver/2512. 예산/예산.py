n = int(input())
arr = sorted(map(int, input().split()))
budget = int(input())

i, j = 0, max(arr)
while i <= j:
    mid = (i+j)//2
    m = 0
    for a in arr:
        if a <= mid:
            m += a
        else:
            m += mid
    if m <= budget:
        i = mid+1
    else:
        j = mid-1
print(j)