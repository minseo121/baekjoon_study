import sys
from collections import deque
input = sys.stdin.readline

def bfs(map_data):
    queue = deque()
    visited = [[0] * m for _ in range(n)]
    queue.append([0, 0])
    visited[0][0] = 1  # 시작점을 방문 처리
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and map_data[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

    print(visited[n-1][m-1])

n, m = map(int, input().split())
map_data = []
for _ in range(n):  
    row = input().strip()  
    map_data.append(list(map(int, row)))

bfs(map_data)
