import sys

data = sys.stdin.readline().split()
n = int(data[0])
m = int(data[1])

dict = {}
dict2 = {}

for i in range(1,n+1):
    name = sys.stdin.readline().strip()
    dict[i] = name
    dict2[name] = i

result = []

for i in range(m):
    b = sys.stdin.readline().strip()
    if b.isdigit(): 
        result.append(dict[int(b)])
    else:
        result.append(str(dict2[b]))

sys.stdout.write("\n".join(result) + "\n")
