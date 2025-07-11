import sys
from collections import defaultdict
input = sys.stdin.readline

count = defaultdict(int)
n = int(input().strip())
data = list(map(int, input().rsplit()))
result = []
mosun = 0

for i in data:
    count[i] += 1
    if i == 0:
        mosun += 1

for i in count:
    if count[i] == i:
        result.append(i)

if result:
    print(max(result))
else:
    if mosun == n:
        print(-1)
    else:
        if 0 in data:
            print(-1)
        else:
            print(0)