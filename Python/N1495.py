import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
v = list(map(int, input().split()))
dp = [[0]*(m+1) for _ in range(n+1)]
#2차원 배열로 각각의 노래의 가능한 불륨을 저장함
#n+1 : 노래 / m+1 가능한 볼륨을 저장하기 위함

dp[0][s] = 1
#시작(0) 볼륨(s)에 1을 넣어주기

for i in range(n):
    #노래마다
    for j in range(m+1):
        #가능한 볼륨 찾아보기기
        if dp[i][j] == 1:
            #그 전 노래에서 가능한 볼륨들이 전부 1로 바뀌어 있을 거기 때문에
            #이를 확인하면서 가능한 볼륨들에 v[i]를 더해주고 빼주기
            min_val = j - v[i]
            max_val = j + v[i]
            if min_val >= 0:
                dp[i+1][min_val] = 1
                #빼준 값이 만약 0이상이라면, 가능하기 때문에 1로 변경
            if max_val <= m:
                dp[i+1][max_val] = 1
                #더해준 값이 만약 m이하라면, 가능하기 때문에 1로 변경

result = -1
#마지막 노래 n까지 도달했을때 해당 배열에 1이 없으면
#마지막 노래까지 도달할 수 없다는 뜻이기 때문에 -1를 미리 넣어주고

for i in range(m, -1, -1):#거꾸로 했을때 가장 먼저 나오는 값이 가장 큰 값이기 때문에
    if dp[n][i] == 1:
        #마지막 노래의 배열에서 1인거 발견하자마자 출력
        result = i
        break
print(result)

