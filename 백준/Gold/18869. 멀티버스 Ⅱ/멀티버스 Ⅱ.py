import sys
input = sys.stdin.readline
from collections import defaultdict

m, n = map(int, input().split())
structure_count = defaultdict(int)

for _ in range(m):
    ps = list(map(int, input().split()))
    sorted_ps = sorted(set(ps))
    pd = {v: i for i, v in enumerate(sorted_ps)}
    rank = tuple(pd[x] for x in ps)
    structure_count[rank] += 1

# 쌍을 만들기 위한 계산 부분
count = 0
for cnt in structure_count.values():
    if cnt >= 2:
        count += cnt * (cnt - 1) // 2

print(count)
