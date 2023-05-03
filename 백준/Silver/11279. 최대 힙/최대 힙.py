import heapq, sys
input = sys.stdin.readline

n = int(input())
maxHeap = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(maxHeap) >= 1:
            print(heapq.heappop(maxHeap)*-1)
        else:
            print(0)
    else:
        heapq.heappush(maxHeap, -x)