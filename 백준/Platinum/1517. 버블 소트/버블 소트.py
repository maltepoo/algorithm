import copy
n = int(input())
nums = list(map(int, input().split()))
swap = 0

#버블정렬
# print(nums)
# bubbleSwap = 0
# for i in range(n):
#     for j in range(i+1, n):
#       if nums[i] > nums[j]:
#           nums[i], nums[j] = nums[j], nums[i]
#           print(nums)
#           bubbleSwap += 1
# print(nums, bubbleSwap)

# arr = copy.deepcopy(nums)
# arrSwap = 0
# for i in range(n - 1, 0, -1):
#     for j in range(i):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             arrSwap += 1
# print(arr, arrSwap)

def merge(left, mid, right):
    global swap

    temp = []  # 정렬된 배열
    l, h = left, mid

    while l < mid and h < right:  # 두(좌, 우)배열이 비교할 원소가 있으면
        if nums[l] <= nums[h]:  # 더 작은수 먼저 배열에 넣어 정렬
            temp.append(nums[l])
            l += 1
        else: # 오른쪽이 더 큰수면 swap되었다는 뜻
            temp.append(nums[h])
            h += 1
            swap += (mid-l) # 몇칸이나 이동했는지
            # [2, 3] [1, 4]를 병합할 때 1-3-2 순으로 이동하므로 스왑2번
            # [2, 3] [4] 2, 3, 4는 이동하지 않으므로 스왑x

    while l < mid: # left 원소가 있으면
        temp.append(nums[l])
        l += 1

    while h < right: # right 원소가 있으면
        temp.append(nums[h])
        h += 1

    for i in range(left, right):
        nums[i] = temp[i - left]  # i의 위치에 있는 원소를 정렬된 원소로 바꿔주기

def divide(st, ed):
    if ed-st <= 1: # 원소 1개이면 분할 끝
        return
    mid = (st+ed)//2
    divide(st, mid)
    divide(mid, ed)
    return merge(st, mid, ed)

divide(0, n)
print(swap)