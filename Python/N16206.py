import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rolls = list(map(int, input().split()))
res = 0
cnt = 0
tens = 0
b = 0

for i in range(n):
    if rolls[i] == 10:
        b += 1
        res += 1
    elif rolls[i] < 10:
        continue
    else:
        if rolls[i] % 10 == 0:
            cnt += ((rolls[i]//10)-1)
        else:
            cnt += ((rolls[i]//10))
        tens += ((rolls[i]//10))

if cnt > m:
    b += cnt - m
    if b != m:
        res += (tens-b)
else:
    res += tens
print(res)
    
