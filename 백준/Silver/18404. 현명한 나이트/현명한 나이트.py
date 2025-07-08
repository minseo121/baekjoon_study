import sys
from collections import deque
input = sys.stdin.readline

def bfs(sx,sy):
    dist = [[-1]*n for _ in range(n)]
    dx = [-2,-2,-1,-1,+1,+1,+2,+2]
    dy = [-1,+1,-2,+2,-2,+2,-1,+1]
    queue = deque()
    queue.append((sx,sy))
    dist[sx][sy] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<= nx<n and 0<=ny<n:
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y]+1
                    queue.append((nx,ny))
    return dist


n, m = map(int, input().rsplit())
sx, sy = map(int, input().rsplit())
sx -= 1
sy -= 1
targets = []
for _ in range(m):
    tx, ty = map(int, input().split())
    targets.append((tx-1,ty-1))

dists = bfs(sx,sy)

result = []
for tx,ty in targets:
    result.append(dists[tx][ty])
    
print(" ".join(map(str, result)))

