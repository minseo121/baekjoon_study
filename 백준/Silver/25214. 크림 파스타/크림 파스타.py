import sys

n = int(input())
a = []
data = list(map(int, sys.stdin.readline().split()))
result = []

mi = data[0]
ma = 0
result.append(0)

for i in range(1, n):
    ma = max(ma, data[i] - mi)
    result.append(ma)
    mi = min(mi, data[i])

sys.stdout.write(" ".join(map(str,result))+' ')
