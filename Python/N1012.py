import sys
from collections import deque

t = int(sys.stdin.readline().strip())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(graph, x, y):
    q = deque()
    q.append([x, y])
    graph[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 1:
                q.append([nx, ny])
                graph[nx][ny] = 0


for _ in range(t):
    m, n, k = map(int, input().split())
    bat = [[0]*n for _ in range(m)] 

    for _ in range(k):
        x, y = map(int, input().split())
        bat[x][y] = 1
    
    cnt = 0
    for j in range(m):
        for k in range(n):
            if bat[j][k] == 1:
                bfs(bat,j,k)
                cnt += 1
    print(cnt)