import sys
input = sys.stdin.readline

n = int(input().strip())
result = []

sosu = [False,False] + [True]* (n+1)
for i in range(2, n+1):
    if sosu[i]:
        result.append(i)
        for j in range(2*i, n+1, i):
            sosu[j] = False

print(result)