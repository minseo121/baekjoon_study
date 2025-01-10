import sys
from collections import deque
input = sys.stdin.readline

def find():
    for i in range(n):
        for j in range(m):
            if campus[i][j] == 'I':
                return(i, j)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    x, y = find()

    campus[x][y] = 'X'

    queue = deque()
    queue.append((x,y))

    count = 0

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            fx, fy = x+dx[k], y +dy[k]
            if (0<=fx<n and 0<=fy<m) and campus[fx][fy] != 'X':
                if campus[fx][fy] == 'P':
                    count+=1
                campus[fx][fy] = 'X'
                queue.append((fx,fy))
    return count

n, m = map(int, input().rstrip().split())
campus = [list(input()) for _ in range(n)]

count = bfs()

if count == 0:
    print('TT')

else:
    print(count)


