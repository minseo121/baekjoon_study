import sys

t = int(sys.stdin.readline().strip())
data = [[1, 0], [0, 1]]

for _ in range(t):
    n = int(sys.stdin.readline().strip())

    while len(data) <= n:
        data.append([
            data[-1][0] + data[-2][0],
            data[-1][1] + data[-2][1]
        ])
    
    sys.stdout.write(f"{data[n][0]} {data[n][1]}\n")
