import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        dp[i+1][j+1] = nums[i][j] + dp[i][j+1] + dp[i+1][j] - dp[i][j]

for _ in range(m):
    a, b, c, d = map(int, input().split())

    result = dp[c][d] - dp[a-1][d] - dp[c][b-1] + dp[a-1][b-1]
    
    print(result)
