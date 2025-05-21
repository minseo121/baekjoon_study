import sys

n = int(input())
size = sys.stdin.readline().split()
num = sys.stdin.readline().split()
setT = int(num[0])
setP = int(num[1])
t = 0
p = n // setP
pn = n%setP

for i in range(6):
    if int(size[i]) % setT == 0:
        t += int(size[i]) // setT
    else:
        t += (int(size[i]) // setT) + 1

print(t)
print(p, pn)