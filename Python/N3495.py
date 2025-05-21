import sys
input = sys.stdin.readline

h, w = map(int, input().split())
maps = [['.']*w for _ in range(h)]

for i in range(h):
    line = input().strip()  
    maps[i] = list(line)  

half = 0
one = 0
for i in range(h):
    lineNum = 0
    for j in range(w):
        if maps[i][j] == '/' or maps[i][j]=='\\':
            half += 1
            lineNum += 1
        else:
            if lineNum % 2 == 1:
                one += 1

print(one+(half//2))