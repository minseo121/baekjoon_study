import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    data = list(map(int, sys.stdin.readline().split()))
    result = 1

    while data:
        if data[0] < max(data):
            data.append(data.pop(0))
        else:
            if m == 0:
                break
            data.pop(0)
            result+=1

        if m > 0:
            m = m-1

        else:
            m=len(data)-1


    print(result)

