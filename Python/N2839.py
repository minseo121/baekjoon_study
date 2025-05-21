import sys

n = int(sys.stdin.readline().strip())
result = [-1]*(n+1)
if n >= 3:
    result[3] = 1
if n >= 5:
    result[5] = 1

for i in range(6, n + 1): 
    if result[i - 3] != -1:
        result[i] = result[i - 3] + 1
    if result[i - 5] != -1:
        if result[i] == -1:
            result[i] = result[i - 5] + 1
        else:
            result[i] = min(result[i], result[i - 5] + 1)

sys.stdout.write(str(result[n]))
