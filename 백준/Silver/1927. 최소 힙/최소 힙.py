import sys
import heapq

n = int(sys.stdin.readline().strip())
heap = []
result = []

for i in range(n):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if not heap:
            result.append(0)
        else:
            num = heapq.heappop(heap)
            result.append(num)
    else:
        heapq.heappush(heap, x)

sys.stdout.write("\n".join(map(str, result)) + "\n")