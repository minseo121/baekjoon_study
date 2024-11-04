import sys
t = int(input())
results = []
dp = [0, 1, 2, 4]

for _ in range(t):
    n = int(input())
    for i in range(len(dp), n+1):
        dp.append((dp[i-3] + dp[i-2]+dp[-1])%1000000009)
    results.append(dp[n])

sys.stdout.write("\n".join(map(str, results)))

#https://my-coding-notes.tistory.com/199 참고