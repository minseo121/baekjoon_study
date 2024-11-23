import sys

n = int(sys.stdin.readline().strip())
v = sys.stdin.readline().split()
v.reverse()
sum = 0
a = 0

for i in range(n):
    if i == 0:
        a = 1
        sum += 1
    else:
        a = min(a+1, int(v[i]))
        sum += a


print(sum)
