import math
import sys

input = sys.stdin.read
data = input().split()

m = int(data[0])
n = int(data[1])
results = []
array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n))+1):
    if array[i] :
        j = 2
        while i*j <= n :
            array[i*j] = False
            j += 1

for i in range(max(2, m), n + 1):
    if array[i] == True:
        results.append(i)

sys.stdout.write("\n".join(map(str, results)) + "\n")
