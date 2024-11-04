import sys

def cnt2(n):
    cnt = 0
    while n != 0:
        n = n//2
        cnt += n
    return cnt

def cnt5(n):
    cnt = 0
    while n != 0:
        n = n//5
        cnt += n
    return cnt

n, m = sys.stdin.readline().split()
n = int(n); m = int(m)

count2 = 0
count5 = 0

count2 = cnt2(n) - (cnt2(m) + cnt2(n-m))
count5 = cnt5(n) - (cnt5(m) + cnt5(n-m))

print(min(count2, count5))