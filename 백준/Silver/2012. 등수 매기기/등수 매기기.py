import sys
input = sys.stdin.readline

n = int(input())
# rank = [0]*(n+1)
# left = []
# disf = 0
# for _ in range(n):
#     pf = int(input())
#     if rank[pf] > 0:
#         left.append(pf)
#     else: rank[pf] += 1
#
# left.sort()
# for i in range(1, n+1):
#     if rank[i] == 0:
#         if left:
#             disf += abs(left.pop(0)-i)
#         else: break
# print(disf)
# n^2 + 불필요한 반복문, List 순회, pop연산 등... 시간초과
# 애초에 받은 수를 정렬한 후 순회하며 idx와 차이값을 누적하면 쉬움

rank = []
disf = 0
for _ in range(n):
    rank.append(int(input()))

rank.sort()
for i in range(1, n+1): # i = 실제 등수로 가정
    disf += abs(rank[i-1]-i)
print(disf)