import sys

k, n = map(int, sys.stdin.readline().strip().split())
data = []
for _ in range(k):
    data.append(int(sys.stdin.readline().strip()))

start, end = 1, max(data)

while(start <= end):
    mid = (start + end) // 2
    line_cnt = 0

    for line in data:
        line_cnt +=  line // mid
    
    if line_cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)