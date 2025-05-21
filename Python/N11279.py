import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())
max_heap = []
result = []

for _ in range(n):
    num = int(input().strip())
    if num == 0:
        if max_heap:
            result.append(-heapq.heappop(max_heap))
        else:
            result.append(0)
    else:
        heapq.heappush(max_heap, -num)

print("\n".join(map(str, result)))
