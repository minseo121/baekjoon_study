import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
tomato =[[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False]*m for _ in range(n)] for _ in range(h)]
queue = deque()
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
result = 0

def bfs():
    while queue:
        x,y,z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue

            if tomato[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
                #이동한 애들이 0(익지 않은 상태)고 방문하지 않았을때
                queue.append((nx,ny,nz))
                #익은 상태로 바꿔주고 이 주변 애들도 바꿔야하기 때문에 큐에 넣어준다.
                #그리고 방문했기 때문에 True로 변경
                tomato[nx][ny][nz] = tomato[x][y][z] + 1
                visited[nx][ny][nz] = True

for a in range(h):
    for b in range(n):
        for c in range(m):
            if tomato[a][b][c] == 1 and visited[a][b][c] == 0:
                #토마토 담은 칸들을 다 돌면서 들어가있는 애들(익은애들)을 큐에 넣어주고 방문했다고 visited를 True로 바꿔주기
                queue.append((a,b,c))
                visited[a][b][c] = True
bfs()

for a in tomato:
    #h층 순회
    for b in a:
        #n개의 줄 순회 
        for c in b:
            #m개의 원소 순회
            if c == 0:
                #c에 0이 있으면~ 익지 않은 토마토가 있는 거기 때문에 -1 print
                print(-1)
                exit(0)
        result = max(result, max(b))
        #가장 늦게 익은 토마토가 얼마나 걸렸나 확인
        
print(result-1)

