import sys

p, m = map(int, sys.stdin.readline().strip().split())
member = []

for _ in range(p):
    data = sys.stdin.readline().split()
    i = int(data[0])
    n = str(data[1])
    member.append([i, n])

index = 0
cnt = 0
results = []

while member:
    if cnt == 0:  # 새로운 방 생성
        room = []
        first = member[index][0]
        level_min = first - 10
        level_max = first + 10
        results.append('Waiting!')
        room.append(member.pop(index))
        cnt += 1
    elif cnt != 0 and cnt < m:  # 방에 멤버 추가\
        if level_min <= member[index][0] and member[index][0]<= level_max:
            room.append(member.pop(index))
            cnt += 1
        else:
            index += 1  # 조건에 맞지 않으면 다음 멤버로 이동
        if index >= len(member):
            index = 0
    if cnt == m:  # 방이 다 찼을 경우
        cnt = 0
        index = 0
        results.pop()  # 'Waiting!' 제거
        results.append('Started!')
        for r in sorted(room, key=lambda x: x[1]):  # 이름순 정렬
            results.append(f"{r[0]} {r[1]}")  

if room:
    for r in sorted(room, key=lambda x: x[1]):
        results.append(f"{r[0]} {r[1]}")

print('\n'.join(results))
