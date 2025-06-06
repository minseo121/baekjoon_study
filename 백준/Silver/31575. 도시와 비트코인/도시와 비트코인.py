import sys
from collections import deque
input = sys.stdin.readline

def bfs(result):
    while queue:
        x, y = queue.popleft()
        if x == n-1 and y == m-1:
            result = True
            break
        else:
            for i in range(2):
                nx, ny = dx[i] + x, dy[i] + y
                if 0<=nx<n and 0<=ny<m and maps[ny][nx] == 1:
                    if nx == n-1 and ny == m-1:
                        result = True
                        break
                    else:
                        maps[ny][nx] = 0
                        queue.append([nx,ny])
    return result

n, m = map(int, input().split())
maps = []
queue = deque([])
dx, dy = [1, 0], [0, 1]
result = False

for _ in range(m):
    maps.append(list(map(int,input().split())))

queue.append([0,0])

if bfs(result):
    print('Yes')
else:
    print('No')