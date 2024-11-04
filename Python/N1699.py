n = int(input())
dp = [i for i in range(n + 1)]

for i in range(2, n+1):
    for j in range(1, i+1):
        a = j*j
        if a > i:
            break
        if dp[i] > dp[i-a]+1:
            dp[i] = dp[i-a]+1

print(dp[n])