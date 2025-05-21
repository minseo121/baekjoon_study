import sys
input = sys.stdin.readline

n, q = map(int, input().split())
a = list(map(int,input().split()))
a.sort()
dp = [0]*(n+1)
dp[0] = a[0]
result = []

for i in range(1,n):
    dp[i]=(dp[i-1]+a[i])
    
for _ in range(q):
    start, end = map(int, input().split())
    if start >= 2:
        print(dp[end-1]-dp[start-2])
    else:
        print(dp[end-1])
