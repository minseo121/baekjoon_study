import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[x][y] = 1
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0 and graph[nx][ny] == graph[x][y]:
                visited[nx][ny] = 1
                q.append((nx,ny))


n = int(input().strip())
graph = [list(input().strip()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
cnt1= 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt1+=1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[0]*n for _ in range(n)]
cnt2= 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt2+=1

print(cnt1, cnt2)