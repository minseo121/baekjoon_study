#dfs는 기본 순회, 최단 경로, 연결 요소, 플러드필 4종류로 구분. 이 문제는 연결 요소 문제로 BFS를 활용하는 것이 좋을 것 같다 판단.
#

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
    