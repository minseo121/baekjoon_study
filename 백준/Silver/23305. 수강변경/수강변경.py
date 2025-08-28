import sys
input = sys.stdin.readline

n = int(input().strip())
a = [0]*1000001
b = [0]*1000001

lecture = list(map(int, input().split())) #가지고 있는 수업
want = list(map(int, input().split())) #갖고 싶은 수업

cnt = 0

for i in range(n):
    a[lecture[i]]+=1
    b[want[i]]+=1


for i in range(1000001):
    if a[i]<b[i]:
        cnt += b[i]-a[i]

print(cnt)