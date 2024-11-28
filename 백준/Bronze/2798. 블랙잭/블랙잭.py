import sys
num = sys.stdin.readline().split()

n = int(num[0])
m = int(num[1])

card = sys.stdin.readline().split()
sum = 0

for i in range(n):
    for j in range(n):
        for l in range(n):
            a = int(card[i])
            b = int(card[j])
            c = int(card[l])
            if i == j or i == l or j == l:
                continue
            elif m-(a+b+c) < 0:
                continue
            else:
                if m-sum > m - (a+b+c):
                    sum = a+b+c

sys.stdout.write(str(sum))