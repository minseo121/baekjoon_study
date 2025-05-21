import sys

data = sys.stdin.readline().split()

n = int(data[0])
k = int(data[1])
b = []
m = 0

for i in range(n):
    a = int(input())
    if k >= a:
        b.append(a)

b.sort(reverse=True)

for coin in b:
    count = k // coin
    k -= count*coin
    m += count
    
print(m)