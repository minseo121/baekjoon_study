import sys

data = sys.stdin.readline().split()
n = int(data[0])
m = int(data[1])

dict = {}

for i in range(0,n):
    site = sys.stdin.readline().split()
    dict[site[0]] = site[1]

result = []

for i in range(m):
    b = input()
    result.append(dict[b])

print("\n".join(result))