import heapq, sys
input = sys.stdin.readline

# 중간수란 물리적으로 중간수가 아니라 1, 5, 2 중 중간 값... (2)
n = int(input())
leftHeap = [] # 중간 값보다 작은 값(최대힙)
rightHeap = [] # 중간 값보다 큰 값(최소힙)
for i in range(n):
    num = int(input())

    if len(leftHeap) == len(rightHeap): # 짝수개를 말했을 때
        heapq.heappush(leftHeap, -num)
    else: # 홀수개를 말했을 때
        heapq.heappush(rightHeap, num)

    if rightHeap and rightHeap[0] < -leftHeap[0]: # 중간값보다 높을때는 교환
        left = heapq.heappop(leftHeap)
        right = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -right)
        heapq.heappush(rightHeap, -left) #최대힙구현을 위해 -값으로 넣었으므로 다시 원래대로 변환
    print(-leftHeap[0])