import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())

graph = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [0]*(n+1)

def bfs(start):
    deq = deque([start])

    while deq:
        node = deq.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = node
                deq.append(i)

bfs(1)

result = visited[2:]
for i in result:
    print(i)

