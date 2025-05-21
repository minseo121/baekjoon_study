import sys

n = int(sys.stdin.readline().strip())
num = []
sum = []

for i in range(n):
    num.append(int(sys.stdin.readline().strip()))

num.sort()

while True:
    if len(num) <= 2:
        sum.append(-1)
        break
    else:
        a = num.pop()
        b = num.pop()
        c = num.pop()
        if a < b + c:
            sum.append(a+b+c)
            break
        elif len(num) == 0:
            sum.append(-1)
            break
        else:
            num.append(c)
            num.append(b)
            continue

sys.stdout.write(str(max(sum)))

