import sys
input = sys.stdin.readline

n = int(input().strip())
k = int(input().strip())
count = 0 

sosu = [0 for i in range(n+1)]
for i in range(2, n+1):
    if sosu[i] == 0:
        for t in range(i, n+1, i):
            if t%i == 0:
                sosu[t] = max(sosu[t],i)

for i in sosu:
    if sosu[i] <= k:
        count += 1

print(count-1)
