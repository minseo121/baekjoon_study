import sys
input = sys.stdin.readline

t = int(input().strip())

while t:
    n = int(input().strip())
    member = list(map(int,input().split())) #팀명 
    teams = [0] *(n+1) #각 팀의 인원 
    s = []
    scores = [0]*(n+1) #각 팀의 정수 배열
    num = 0
    for i in range(0, n):
        teams[member[i]] += 1 #들어오는 팀명들의 팀들의 인원을 들어올때마다 추가해줌 

    for i in range(0, n):
        if teams[i] >= 6: #그렇게 들어온 값이 6이상이라면
            s.append(i) #그 해당 index값을 s 배열에 추가

    count = [0]*(n+1)
    for i in range(0, n):
        if member[i] not in s: #6이상인 팀들을 모은 s배열에 member[i]가 없으면
            num += 1 #수를 1씩 더함 
        else:
            if count[member[i]] > 4: #만약 해당 팀을 4번 넘게 카운트했으면 다음으로 띵기기
                continue
            h = i-num #num에 들어있는 수는, 점수 계산에 제외되어야하는 값들을 추가한 것
            scores[member[i]] += h #진행한 진행도(i)에 제외되어야하는 값(num)이 빠진 h 값을 scores에 추가 
            count[member[i]] += 1 #4번째까지 합하는 것이므로 횟수 추가

    minNum = 0
    result = 0
    for i in range(0, n):
        if scores[i] != 0:
            if result == 0:
                minNum = scores[i]
                result = i
            else:
                if minNum > scores[i]:
                    minNum = scores[i]
                    result = i
                elif minNum == scores[i]:
                    result = member[4]

    print(result)

    t-=1
