import sys
from collections import deque
input = sys.stdin.readline

def bfs():
  queue = deque()
  queue.append(n)
  while queue:
    x = queue.popleft()
    if x == k:
      print(visited[x])
      break
    for j in (x-1, x+1, 2*x):
      if 0 <= j <= max_num and not visited[j]:
        visited[j] = visited[x]+1
        queue.append(j)
  

n, k = map(int, input().split())
max_num = 100000
visited = [0]*(max_num+1)

bfs()

