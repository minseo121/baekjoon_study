import sys

n = int(input())

data = []
result = []

for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    count = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1
    result.append(count + 1)

sys.stdout.write(" ".join(map(str, result)))