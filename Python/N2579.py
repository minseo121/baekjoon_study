import sys

n = int(sys.stdin.readline().strip())
stairs = []
results = [0] * n

for _ in range(n):
    stairs.append(int(sys.stdin.readline().strip()))

if n == 1:
    print(stairs[0])
    sys.exit()

results[0] = stairs[0] 
results[1] = stairs[0] + stairs[1] 
if n > 2:
    results[2] = max(stairs[0]+stairs[2],stairs[1]+stairs[2])

for i in range(3, n):
    results[i] = max(results[i-2]+stairs[i], results[i-3]+stairs[i-1]+stairs[i])

sys.stdout.write(str(results[n-1]))