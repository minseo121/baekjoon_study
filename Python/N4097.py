import sys
input = sys.stdin.readline

while True:
    n = int(input().strip())

    if n == 0:
        break
    else:
        result = [0] * n
        for i in range(n):
            if i == 0:
                result[i] = int(input().strip())
            else:
                a = int(input().strip())
                result[i] = max(a, result[i-1]+a)
        print(max(result))