import sys
input = sys.stdin.readline

data = []

for _ in range(3):
    x, y = map(int, input().split())
    data.append([x,y])

if data[0][0]/data[0][1] == data[1][0]/data[1][1] == data[2][0]/data[2][1]:
    print("WHERE IS MY CHICKEN?")
elif data[0][0] == data[1][0] == data[2][0] or data[0][1] == data[1][1] == data[2][1]:
    print("WHERE IS MY CHICKEN?")
else:
    print("WINNER WINNER CHICKEN DINNER!")

