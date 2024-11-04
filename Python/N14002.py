n = int(input())
a = list(map(int, input().split()))
dp = [0] * n
result = []

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))
order = max(dp)

for i in range(n-1, -1, -1):
    if dp[i] == order:
        result.append(a[i])
        order -= 1

result.reverse()
print(*result)