import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().rsplit())))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    queue = deque()
    sido = [row[:] for row in maps]
    #백트래킹을 해줘야하기 때문에
    #깊은 복사를 해야함
    #얕은 복사를 하게 되면 sido가 바뀔때 maps도 같이 바뀜. (같은 객체를 참조하기 때문)

    for i in range(n):
        for j in range(m):
            if sido[i][j] == 2:
                queue.append((i,j))
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<= nx<n and 0<= ny<m and sido[nx][ny] == 0:
                sido[nx][ny] = 2
                queue.append((nx,ny))

    cnt = 0
    for i in range(n):
        cnt += sido[i].count(0)
    global ans
    ans = max(ans, cnt)

def makewall(cnt):
    if cnt == 3:
        bfs()
        return
    else:
        for i in range(n):
            for j in range(m):
                if maps[i][j] == 0:
                    maps[i][j] = 1
                    makewall(cnt + 1)
                    maps[i][j] = 0 #백트래킹 과정

ans = 0
makewall(0)
print(ans)