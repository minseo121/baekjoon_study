import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

#확인하기 위해 정리
#box1 = [(x1,y1),(x1,y2),(x2,y2),(x2,y1)]
#box2 = [(x3,y3),(x3,y4),(x4,y4),(x4,y3)]

#Point 조건
if (x1, y1) == (x4, y4) or (x1,y2) == (x4,y3) or (x3, y3) == (x2,y2) or (x2,y1) == (x3,y4):
    print('POINT')

#Line 조건
elif x1 == x4 or x2 == x3 or y1 == y4 or y2 == y3:
    print('LINE')

#Face 조건
elif x1 <= x3 <= x2 or x1 <= x4 <= x2 or x3 <= x1 <= x4 or x3 <= x2 <= x4:
    if y1 <= y3 <= y2 or y1 <= y4 <= y2 or y3 <= y1 <= y4 or y3 <= y2 <= y4:
        print('FACE')

#예외조건
else:
    print('NULL')