import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
queue = deque()
line = 0
maxLine = 0
studentId = n
for _ in range(n):
    data = list(map(int, input().split()))
    if data[0] == 1:
        queue.append(data[1])
        line += 1
        if maxLine < line:
            maxLine = line
            studentId = data[1]
        elif maxLine == line:
            if studentId > data[1]:
                studentId = data[1]
    else:
        queue.popleft()
        line -= 1

print(maxLine,studentId)