import sys
input = sys.stdin.readline

n, m = map(int,input().split())
data = []
state = True

for i in range(m):
    k = int(input())
    data.append(list(map(int, input().split())))

for i in range(m):
    num = 0
    for j in range(len(data[i])):
        if j == 0:
            num = data[i][j]
        if data[i][j] > num:
            state = False
            break
        else:
            num = data[i][j]
    if state == False:
        break

if state:
    print("Yes")
else:
    print("No")

