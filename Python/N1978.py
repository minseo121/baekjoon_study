import math
import sys

def sosu(a):
    if a < 2:
        return 0
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return 0
    return 1

input = sys.stdin.read
data = input().split()

n = int(data[0])
e = 0
for i in range(1, n + 1):
    e += sosu(int(data[i]))

print(e)
