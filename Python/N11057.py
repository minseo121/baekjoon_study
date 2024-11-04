n = int(input())
dp = [[0] * 10 for _ in range(n)]  
total_sum = 0  

for j in range(10):
    dp[0][j] = 1 

for i in range(1, n):
    for j in range(10):
        if j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]


for j in range(10):
    total_sum += dp[n-1][j]

print(total_sum%10007) 