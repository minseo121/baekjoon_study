import sys
from collections import deque
input = sys.stdin.readline

def bfs(computer):
    visited = [1]
    count = 0
    queue = deque()
    queue.append(1)
    while queue:
        a = queue.popleft()
        for i in computer[a]:
            if i not in visited:
                visited.append(i)
                count += 1
                queue.append(i)
                
    return count

n = int(input().strip())
m = int(input().strip())
computer = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)

print(bfs(computer))