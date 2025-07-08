import sys
input = sys.stdin.readline

lista = input().rstrip()
listb = input().rstrip()

n = len(lista)
m = len(listb)
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if lista[i-1] == listb[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][m])