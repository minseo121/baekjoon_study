import sys

n = int(input())
data = [sys.stdin.readline().strip() for _ in range(n)]

set_data = set(data)
data = list(set_data)
data.sort()
data.sort(key = len)

sys.stdout.write("\n".join(map(str, data)) + "\n")
    