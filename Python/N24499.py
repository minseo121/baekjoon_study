import sys
input = sys.stdin.readline

n, k = map(int, input().split())
taste = list(map(int, input().split()))
s = sum(taste[:k])
#배열은 0에서부터 시작하기 때문에 k전까지 일단 먼저 더해주기 => 맨 첨 합 구함
result = s

for i in range(k, n+k):
    num = i%n
    #n+k가 n을 넘기 때문에, 나머지로 배열 돌아가는 걸 확인
    s+=taste[num]
    #그렇게 넘어간 num번째 값을 s에 추가해주고
    s-=taste[num-k]
    #한칸씩 이동했기 때문에 지나간 num-k 값은 빼준다.
    result = max(s, result)
    #이렇게 구한 s의 값이랑 기존 result 값을 비교해서 둘 중 큰 값을 result에 넣어줌

print(result)
#쫙 다 돌았을때 result 출력
