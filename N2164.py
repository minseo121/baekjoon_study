import sys
from collections import deque

n = int(sys.stdin.readline().strip())
que = deque(range(1, n + 1))

while len(que) > 1:
    que.popleft()
    que.append(que.popleft())

sys.stdout.write(str(que.popleft()) + "\n")
