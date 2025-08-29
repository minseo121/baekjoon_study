import sys
input = sys.stdin.readline
from collections import Counter

t = int(input().strip())
x = 1

while t:
    n = int(input().strip())
    p = list(map(int, input().rsplit()))
    cnt = Counter(p)
    res = []
    for i in p:
        if cnt[i] == 0:
            continue

        real_i = i*4
        real_i //= 3
        if real_i in p and cnt[real_i] > 0:
            res.append(i)
            cnt[i] -= 1
            cnt[real_i] -= 1
        else:
            cnt[i] -= 1
    
    print(f"Case #{x}: {' '.join(map(str,res))}")
    t-=1
    x+=1
