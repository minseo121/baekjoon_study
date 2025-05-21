import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(key=lambda x: (x % 10, x))  # 10으로 나눴을 때의 나머지로 오름차순
ans = 0

for a in arr:
    if a % 10 == 0:
        cutting = a//10 - 1
        if cutting > m:
            ans += m
        else:
            ans += (cutting+1)
    else:
        cutting = a//10
        if cutting > m:
            ans += m
        else:
            ans += cutting
    m -= cutting
    if m <= 0:
        break
print(ans)