import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

remimder = [0]*m
prefix_sum = 0
for i in range(n):
    prefix_sum += arr[i]
    remimder[prefix_sum % m] += 1 # 나눴을때 나머지가 res의 index

answer = remimder[0] # 이미 나누어 떨어진경우 추가
for j in remimder:
    answer += j*(j-1)//2 # 경우의수

print(answer)