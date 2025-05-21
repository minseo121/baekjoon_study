import sys
input = sys.stdin.readline

n, r = list(map(int, input().rstrip().split()))
print((n+1)+(r-1)*2)