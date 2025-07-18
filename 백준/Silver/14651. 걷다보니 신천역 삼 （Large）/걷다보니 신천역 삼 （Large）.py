import sys
input = sys.stdin.readline

n = int(input().strip())

dp = [0]*33334
num = 1000000009

dp[0] = 0
dp[1] = 2
dp[2] = 6

for i in range(3, n):
    dp[i] = (dp[i-1]*3)%num

print(dp[n-1])