import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
nods = list(map(int, input().split()))
a = (n - v) + 1

for i in range(m):
    order = int(input().strip())
    if order < n:
        print(nods[order])
    else:
        order = (order - n) % a
        print(nods[v - 1 + order])