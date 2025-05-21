import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(mapData, a, b):
    queue = deque()
    queue.append([a,b])
    mapData[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            if 0 <= nx < n and 0 <= ny <n and mapData[nx][ny] == 1 and mapData[nx][ny] == 1:
                queue.append([nx,ny])
                mapData[nx][ny] = 0
                count += 1

    return count

n = int(input().strip())
mapData = []
result = []
for _ in range(n):
    row = input().strip()
    mapData.append(list(map(int, row)))

for i in range(n):
    for j in range(n):
        if mapData[i][j] == 1:
            result.append(bfs(mapData, i, j))

result.sort()

print(len(result))
for i in range(len(result)):
    print(result[i])

