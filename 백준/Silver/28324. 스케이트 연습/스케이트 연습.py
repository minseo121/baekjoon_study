import sys

n = int(sys.stdin.readline().strip())
v = sys.stdin.readline().split()
sum = 0
v[n-1] = 1

for i in range(n):
    if i != n-1:
        m = int(v[i])
        for j in range(n-i):
            if m > int(v[i+j])+j:
                m = int(v[i+j])+j
        sum += m
    else:
        sum+=1

print(sum)