import sys
input = sys.stdin.readline

n = int(input().strip())
dp = [0]*(n+1)
dp[1] = 1
dp[2] = 2
dp[3] = 2
dp[4] = 4
dp[5] = 4
for i in range(6, n+1):
    if i % 2 == 0:
        dp[i] = (dp[i-3]+dp[i-1])%1000000000
    else:
        dp[i] = (dp[i-1])%1000000000

print(dp[n])