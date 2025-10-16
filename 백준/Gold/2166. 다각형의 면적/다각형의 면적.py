import sys
input = sys.stdin.readline

n = int(input().strip())
dot = []
result = 0

for i in range(n):
    dot.append(list(map(int, input().split())))
dot.append(dot[0])

for i in range(n):
    result += dot[i][0]*dot[i+1][1] - dot[i+1][0]*dot[i][1]

print(abs(result)/2)