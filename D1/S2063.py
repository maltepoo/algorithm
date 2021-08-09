#2063. 중간값 찾기
n, nums = int(input()), list(map(int,input().split()))
nums.sort()
print(nums[(n // 2)])