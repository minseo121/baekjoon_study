import sys
input = sys.stdin.readline

def find(a, b):
    if not ji[a][b] == '*':
        x=a
        y=b
        num = 0
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and ji[nx][ny] == "*":
                num+=1
        results[a][b] = num

n = int(input().strip())
ji = []
game = []
results = [[0]*n for _ in range(n)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
gameOver = False

for _ in range(n):
    ji.append(input())
for _ in range(n):
    game.append(input())

for i in range(n):
    for j in range(n):
        find(i,j)

for i in range(n):
    for j in range(n):
        if game[i][j] == 'x':
            if ji[i][j] == '*':
                gameOver = True
                results[i][j] = '*'
        else:
            if not gameOver:
                results[i][j] = '.'
            else:
                if ji[i][j] == '*':
                    results[i][j] = '*'
                else:
                    results[i][j] = '.'

if gameOver:
    for i in range(n):
        for j in range(n):
            if ji[i][j] == '*':
                results[i][j] = '*'

for i in range(n):
    print("".join(map(str,results[i])))