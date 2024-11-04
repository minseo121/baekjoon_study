n, k = map(int, input().split())

dp = [[0] * (n + 1) for _ in range(k + 1)]

# k = 1일 때는 n을 만드는 방법은 무조건 1가지
for i in range(k + 1):
    dp[i][0] = 1

for i in range(1, k + 1):
    for j in range(1, n + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1])%1000000000

print(dp[k][n])
