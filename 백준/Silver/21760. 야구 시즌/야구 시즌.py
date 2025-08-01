import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n, m, k, d = map(int, input().rsplit())
    
    num = n*m*((m-1)*k+(n-1)*m)//2
    B = d // num
    A = k*B

    if B <= 0:
        result = -1
    else:
        result = num*B

    print(result)