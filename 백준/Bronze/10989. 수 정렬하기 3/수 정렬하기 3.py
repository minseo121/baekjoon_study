import sys

n = int(sys.stdin.readline().strip())
arr = [0] * (10000+1)

for _ in range(n):
    arr[int(sys.stdin.readline().strip())] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            sys.stdout.write(str(i)+"\n")
            