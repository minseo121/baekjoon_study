import sys
from collections import deque

n, q = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))
index = 0

for _ in range(q):
    data = list(map(int, sys.stdin.readline().strip().split()))
    if data[0] == 1:
        a[(index + data[1]-1)%n] += data[2]
    if data[0] == 2:
        index -= data[1]
    if data[0] == 3:
        index += data[1]

for i in range(index, index+n):
    sys.stdout.write(str(a[i%n])+ ' ')