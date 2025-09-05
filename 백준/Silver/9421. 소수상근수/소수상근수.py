import sys
input = sys.stdin.readline

def check(num):
    visit = {}
    while 1:
        n = str(num)
        num = 0
        for i in range(len(n)):
            num += int(n[i])*int(n[i])

        if num == 1:
            return True
        elif num in visit:
            return False
        else:
            visit[num] = 1

n = int(input().strip())
isPrime=[True]*(n+1)

for i in range(2, n+1):
    if isPrime[i]:
        for j in range(i+i, n+1, i):
            isPrime[j] = False

for i in range(7, n+1):
    if isPrime[i]:
        if check(i):
            print(i)