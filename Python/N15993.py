import sys
input = sys.stdin.readline

dp = [0]*100001
MOD = 1000000009

dp[0] = 1
dp[1] = 2
dp[2] = 4

for i in range(3, 100001):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1])%MOD


t = int(input().strip())
results = []
for _ in range(t):
    n = int(input().strip())-1
    a = (dp[n]//2)%MOD
    if n % 2 == 0:
        if dp[n] % 2 == 0:
            results.append(f"{a} {a}")
        else:
            results.append(f"{a+1} {a}")
    else:
        if dp[n] % 2 == 0:
            results.append(f"{a} {a}")
        else:
            results.append(f"{a} {a+1}")

sys.stdout.write("\n".join(results) + "\n")

