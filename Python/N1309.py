n = int(input())

if n == 1:
    print(3)
else:
    dp=[1 for _ in range(n+1)]
    dp[1], dp[2] = 3, 7
    for i in range(3, n+1):
        dp[i] = (2*dp[i-1] + dp[i-2])%9901
        #점화식 맞췄다ㅜㅜ

    print(dp[n])
