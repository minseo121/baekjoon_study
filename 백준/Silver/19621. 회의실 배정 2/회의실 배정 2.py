import sys
input=sys.stdin.readline

n = int(input().strip())
meeting = []

for _ in range(n):
    a, b, c = map(int, input().rstrip().split())
    meeting.append((a,b,c))

meeting.sort()

dp = [0]*n
dp[0] = meeting[0][2]
for i in range(1, n):
    dp[i] = max(dp[i-1], dp[i-2]+meeting[i][2])
#이게 가능한 이유는 제한 두번째 확인

print(dp[n-1])