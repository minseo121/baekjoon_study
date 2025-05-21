import sys
input = sys.stdin.readline

t = int(input().strip())

max_n = 1000
max_m = 1000
dp = [[0]*(max_n+1) for _ in range(max_m+1)]
dp[1][1] = 1
dp[1][2] = 1
dp[1][3] = 1
dp[2][2] = 1
for i in range(2, max_m+1):
    for j in range(3, max_n+1):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j-2] + dp[i-1][j-3])%1000000009

while t:
    n, m = map(int, input().split())
    print(dp[m][n])
    t-=1