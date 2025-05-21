import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [0] * 101 
visited = [0] * 101

l = dict()
s = dict()

for _ in range(n):
    a, b = map(int, input().split())
    l[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    s[a] = b

q = deque([1])

while q:
    x = q.popleft()
    if x == 100:
        print(board[x])
        break
    for i in range(1,7):
        next = x+i
        if next <= 100 and not visited[next] == 1:
            if next in l.keys():
                next = l[next]
            if next in s.keys():
                next = s[next]
            if not visited[next] == 1:
                board[next] = board[x] + 1
                visited[next] = 1
                q.append(next)