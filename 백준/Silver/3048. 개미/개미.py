import sys
input = sys.stdin.readline

n1,n2= map(int, input().split())
g1 = input().strip()
g2 = input().strip()
t = int(input().strip())
result = []

for i in range(n1-1, -1, -1):
    result.append(g1[i])
for i in range(n2):
    result.append(g2[i])

while t != 0:
    num = []
    for i in range(len(result)-1):
        if result[i] in g1:
            if result[i+1] in g2:
                num.append(i)
    for j in num:
        a = result[j+1]
        result[j+1] = result[j]
        result[j] = a
    t-=1

print("".join(map(str, result)))