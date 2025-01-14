import sys

n = int(sys.stdin.readline().strip())
v = int(sys.stdin.readline().strip())
computer = [[] for i in range(n+1)]
visited = [0]* (n+1)

for _ in range(v):
    a, b = map(int, input().split())
    computer[a] += [b]
    computer[b] += [a]

def dfs(v):
    visited[v] = 1
    for num in computer[v]:
        if visited[num] == 0:
            dfs(num)

dfs(1)
print(sum(visited)-1)