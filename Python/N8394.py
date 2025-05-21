import sys
input = sys.stdin.readline

n = int(input().strip())

count = 0

visited = [0]*(n-1)
visited[0] = 0
for i in range(1, n-1):
    if visited[i-1] == 0:
        visited[i] = 1
        count += 1
    elif visited[i-1] == 1:
        visited[i] = 0
        count += 1

visited = [0]*(n-1)
visited[0] = 1
for i in range(1, n-1):
    if visited[i-1] == 0:
        visited[i] = 1
        count += 1
    elif visited[i-1] == 1:
        visited[i] = 0
        count += 1

for i in range(1, n-1):
    if visited[i-1] == 0:
        if visited[i] == 1:
            visited[i] = 0
            count += 1

print(count)