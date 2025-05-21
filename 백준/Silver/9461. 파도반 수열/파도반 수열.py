import sys

t = int(sys.stdin.readline().strip())
result = []

for i in range(t):
    n = int(sys.stdin.readline().strip())
    data = [1]*n
    for j in range(n):
        if j > 2:
            data[j] = data[j-2] + data[j-3]
    result.append(data[n-1])

sys.stdout.write("\n".join(map(str, result)) + "\n")