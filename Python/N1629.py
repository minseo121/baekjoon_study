import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def reduce(a, b, c):
    if (b == 1):
        return a % c

    res = reduce(a, b//2, c)

    if (b % 2 == 0):
        return res * res % c
    else:
        return a * res * res % c

print(reduce(a,b,c))
