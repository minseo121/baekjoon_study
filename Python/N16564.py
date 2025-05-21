import sys
input = sys.stdin.readline

n, k = map(int, input().split())               # n: 캐릭터(또는 플레이어) 수, k: 올릴 수 있는 총 레벨 포인트
levels = [int(input()) for _ in range(n)]       # 각 캐릭터의 현재 레벨을 리스트로 입력받음

# 이진 탐색을 위한 초기 범위 설정
s, e = min(levels), max(levels) + k             # 최소 레벨부터 (최대 레벨 + 남은 포인트)까지 탐색
result = 0                                      # 가능한 최대 목표 레벨을 저장할 변수

while s <= e:
    goal_level = (s + e) // 2                   # 현재 시도할 목표 레벨을 중간값으로 설정
    need_level = 0                              # 목표 레벨까지 올리는데 필요한 총 포인트 합계 초기화

    # 각 캐릭터가 goal_level까지 레벨업 하는데 필요한 포인트 계산
    for lv in levels:
        if goal_level > lv:
            need_level += goal_level - lv      # lv가 작을 때만 (차이만큼) 더함

    if need_level <= k:
        # k 이내로 레벨업이 가능하다면 결과 갱신 & 하한(s)을 올려 더 높은 목표 시도
        result = goal_level
        s = goal_level + 1
    else:
        # k를 초과하면 목표를 낮춰야 하므로 상한(e)을 내림
        e = goal_level - 1

print(result)  # 올릴 수 있는 최대 목표 레벨 출력
