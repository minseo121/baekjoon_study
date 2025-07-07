import sys
from collections import defaultdict
input = sys.stdin.readline

n=int(input().strip())
for _ in range(n):
    data = list(map(int, input().split()))
    t = data[0]
    s = data[1:]

    count = defaultdict(int)
    for i in s:
        count[i] += 1

    h = t//2
    found = False
    for i in count:
        if count[i] > h:
            print(i)
            found = True
            break
    if not found:
        print("SYJKGW")
