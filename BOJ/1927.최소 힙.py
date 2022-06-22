import sys
import heapq
n = int(sys.stdin.readline())
min_heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(min_heap) > 0:
            print(heapq.heappop(min_heap))
        else: print(0)
    else:
        heapq.heappush(min_heap, x)