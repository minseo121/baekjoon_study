import sys

data = sys.stdin.readline().split()
n = int(data[0])
m = int(data[1])

dict = {}

for i in range(1,n+1):
    name = input()
    dict[i] = name
    dict[name] = i

for i in range(m):
    b = sys.stdin.readline().strip()
    if b.isdigit(): 
        b= int(b)
    sys.stdout.write(str(dict[b]) + '\n')
