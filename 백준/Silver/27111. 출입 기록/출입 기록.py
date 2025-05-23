import sys
input = sys.stdin.readline

n = int(input())
member = [0]*200001
count = 0
for i in range(n):
    data = list(map(int, input().split()))
    if data[1] == 1:
        if member[data[0]] != 1:
            member[data[0]] = 1
        else:
            count += 1
    if data[1] == 0:
        if member[data[0]] == 0:
            count += 1
        else:
            member[data[0]] = 0

for i in range(len(member)):
    if member[i] != 0:
        count+=1

print(count)


