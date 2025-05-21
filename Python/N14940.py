import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, visited, start):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1 and graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y]+1; #방문표시
                    queue.append((nx, ny))

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] *m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start = (i,j)
        elif graph[i][j] == 0:
            visited[i][j] = 0

bfs(graph, visited, start)

for i in range(n):
    for j in range(m):
        print(visited[i][j], end=' ')
    print('')