import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort()

d = [-1]*(n+1) #깊이
t = [0] * (n+1) #순서

dq = deque([r]) #시작 노드 덱에 넣어주기
d[r] = 0 #시작지점의 깊이는 0
cnt = 1
t[r] = cnt #시작지점의 방문 순서는 1

while dq: #덱에 값이 있을때까지
    u = dq.popleft()
    for v in graph[u]: #다음 노드로 넘어가는 노드값들
        if d[v] == -1: #아직 방문을 안한 노드라면
            d[v] = d[u]+1 #이전 노드 +1 
            cnt += 1 
            t[v] = cnt #이전 방문 횟수 +1
            dq.append(v) #새로 방문할 노드들 덱에 넣어주기

ans = sum(d[i]*t[i] for i in range(1, n+1))
print(ans)
