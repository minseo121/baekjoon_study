import sys
input = sys.stdin.readline

a, b, d = map(int, input().rsplit())
isPrime = [True] * (b+1)
cnt = 0

isPrime[0] = False
isPrime[1] = False

for i in range(2, b+1):
    if isPrime[i]:
        for j in range(i+i, b+1, i):
            isPrime[j] = False

for i in range(a, b+1):
    if isPrime[i] and str(d) in str(i):
        cnt += 1

print(cnt)
