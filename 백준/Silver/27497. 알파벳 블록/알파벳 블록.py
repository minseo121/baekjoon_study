import sys
input = sys.stdin.readline
from collections import deque

n = int(input().strip())
deq = deque()
memo = []

for _ in range(n):
    data = input().split()
    num = int(data[0])
    if num == 1:
        deq.append(data[1])
        memo.append(0)
    elif num == 2:
        deq.appendleft(data[1])
        memo.append(1)
    else:
        if memo:
            if deq:
                m = memo.pop()
                if m == 1:
                    deq.popleft()
                else:
                    deq.pop()

if deq:
    print(''.join(deq))
else:
    print(0)
