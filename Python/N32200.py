import sys

data = sys.stdin.readline().split()
n = int(data[0])
x = int(data[1])
y = int(data[2])
length=list(map(int,sys.stdin.readline().split()))

ma = 0 #샌드위치로 해결가능한 끼니의 최대 / 즉 x,y범위에서 최소 사용
mi = 0 #버려지는 조각 길이의 합의 최소 / 잘라먹었을때 남는 다는 가정 하에 x,y 범위에서 최대 사용

for i in range(n):
    send = length[i]
    if send >= x:
        ex = send
        index = y
        while True:
            if ex >= index:
                ex = ex-index
                ma += 1
            else:
                index -= 1
                if index < x:
                    break
        mi += ex
    else:
        mi += send

sys.stdout.write(str(ma)+  "\n")
sys.stdout.write(str(mi))
