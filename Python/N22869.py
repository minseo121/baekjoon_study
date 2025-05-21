import sys
from collections import deque
input = sys.stdin.readline


n, k = map(int, input().split())
d = list(map(int, input().split()))
reached = [0]*(n+1)

dq = deque([1])
reached[1] = 1
while dq:
    i = dq.popleft()
    for j in range(i+1 ,n+1):
        if (j - i) * (1 + abs(d[i-1]-d[j-1])) <= k and not reached[j]:
            reached[j] = 1
            dq.append(j)

if reached[n] == 1:
    print("YES")
else:
    print("NO")