import sys
input = sys.stdin.readline

def binary_search(target, b):
    start, end = 0, m - 1

    while start <= end:
        mid = (start + end) // 2
        if target == b[mid]:
            return b[mid]
        elif target > b[mid]:
            start = mid + 1
        else:
            end = mid - 1

    if start >= m:
        return b[end]

    elif end < 0:
        return b[start]

    else:
        if abs(b[start] - target) < abs(b[end] - target):
            return b[start]
        else:
            return b[end]
        
t = int(input().strip())

for _ in range(t):
    n, m = map(int, input().rsplit())
    a = list(map(int, input().rsplit()))
    b = list(map(int, input().rsplit()))
    b.sort()
    c = []
    
    for i in range(n):
        close = binary_search(a[i], b)
        c.append(close)

    print(sum(c))