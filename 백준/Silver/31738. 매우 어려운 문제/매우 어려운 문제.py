import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = 1

if n > m :
    print(0)
else:
    for i in range(1, n+1):
        result = (result*i)%m
    print(result)
