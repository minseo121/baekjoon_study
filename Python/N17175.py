import sys
input = sys.stdin.readline

n = int(input().strip())

f = []

f.append(1)
f.append(1)

for i in range(2,n+1):
    f.append(f[i-2] + f[i-1] + 1) 

print(f[n]%1000000007)
