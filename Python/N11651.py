import sys

n = int(input())
data = []
result = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    data.append((x,y))

data.sort(key = lambda x :(x[1],x[0]))

for d in data:
    print(d[0], d[1])