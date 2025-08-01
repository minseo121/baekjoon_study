import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n, m, k, d = map(int, input().rsplit())

    B = d // (k*(m*(m-1))+m*m)
    A = k*B
    result = A*((m-1)*m)+B*(m*m)
    if B == 0:
        result = -1

    print(result)