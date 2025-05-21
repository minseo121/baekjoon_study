import sys
input = sys.stdin.readline

# 입력 받기
n = int(input().strip())  # 데이터 크기
data = [['.'] * n for _ in range(n)]  # 초기 빈 데이터
message = input().strip()  # 이동 명령어
x, y = 0, 0  # 시작 위치

# 이동 처리
for m in message:
    if m == 'D':  # 아래로 이동
        if x + 1 < n:  # 경계값 확인
            for j in range(2):
                if data[x][y] == '-':
                    data[x][y] ='+'
                elif data[x][y] == '.':
                    data[x][y] = '|'
                if j == 0:
                    x += 1
                    
    elif m == 'U':  # 위로 이동
        if x - 1 >= 0:  # 경계값 확인
            for j in range(2):
                if data[x][y] == '-':
                    data[x][y] ='+'
                elif data[x][y] == '.':
                    data[x][y] = '|'
                if j == 0:
                    x -= 1
    elif m == 'L':  # 왼쪽으로 이동
        if y - 1 >= 0:  # 경계값 확인
            for j in range(2):
                if data[x][y] == '|':
                    data[x][y] ='+'
                elif data[x][y] == '.':
                    data[x][y] = '-'
                if j == 0:
                    y -= 1
    elif m == 'R':  # 오른쪽으로 이동
        if y + 1 < n:  # 경계값 확인
            for j in range(2):
                if data[x][y] == '|':
                    data[x][y] ='+'
                elif data[x][y] == '.':
                    data[x][y] = '-'
                if j == 0:
                    y += 1
    
for row in data:
    print(''.join(row))
