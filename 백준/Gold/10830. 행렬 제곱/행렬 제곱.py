import sys
input = sys.stdin.readline

n, b = map(int, input().rsplit())
num = []
for _ in range(n):
    num.append(list(map(int, input().split())))
mod = 1000

def multi(n, a, b):
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += (a[i][k] * b[k][j])
            result[i][j] %= mod
    return result

def cal(n, b, a):
    if b == 1:
        return a
    elif b == 2:
        return multi(n, a, a)
    else:
        temp = cal(n, b//2, a)
        if b % 2 == 0:
            return multi(n, temp, temp)
        else:
            return multi(n, multi(n, temp, temp), a)

result = cal(n, b, num)

for row in result:
    print(" ".join(str(num % 1000) for num in row))