import sys
input = sys.stdin.readline

n = int(input().strip())
num = []
num.append(0)
dp = [0]*(n+1)
for _ in range(n):
    a = list(map(int, input().rsplit()))
    num.append(a[2])

if n >= 1:
    dp[1] = num[1]
if n >= 2:
    dp[2] = max(num[1], num[2])
    
for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-2]+num[i])

print(max(dp))