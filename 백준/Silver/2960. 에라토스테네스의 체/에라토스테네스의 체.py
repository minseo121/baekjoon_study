import sys
input = sys.stdin.readline

n, k = map(int,input().split())
result = 0

sosu = [True] * (n+1)
for i in range(2, n+1):
    for j in range(i, n+1, i):
        if sosu[j] != False:
            sosu[j] = False
            result += 1
            if result == k:
                print(j)