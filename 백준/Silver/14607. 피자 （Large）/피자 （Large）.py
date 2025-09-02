import sys
input = sys.stdin.readline

n = int(input().strip())
n = n*(n-1)//2
if n == 0:
    print(0)
else:
    print(n)