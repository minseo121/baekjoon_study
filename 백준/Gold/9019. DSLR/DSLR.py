import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    visited = [False for i in range(10001)]

    queue = deque([(A, "")])

    visited[A] = True

    while queue:
        n, command = queue.popleft()
        if n == B:
            print(command)
            break
        D = (n * 2) % 10000
        if not visited[D]:
            visited[D] = True
            queue.append((D, command + "D"))
        if n > 0:
            S = n - 1
        else:
            S = 9999
        if not visited[S]:
            visited[S] = True
            queue.append((S, command + "S"))
        L = n // 1000 + (n % 1000) * 10
        if not visited[L]:
            visited[L] = True
            queue.append((L, command + "L"))
        R = (n % 10) * 1000 + n // 10
        if not visited[R]:
            visited[R] = True
            queue.append((R, command + "R"))