import sys
input = sys.stdin.readline

n, r = list(map(int, input().rstrip().split()))
num = (n*r)+1
status = False

while True:
    for i in range(num):
        a = (num-i)
        b = i
        if a > r or b > r:
            status = True
        else:
            status = False
            break
    if status:
        break
    else:
        num += 1
#시간 초과 안나게 어떻게 하지?
print(num)