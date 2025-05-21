import sys
input = sys.stdin.readline

n, k = list(map(int, input().rstrip().split()))
s = [int(i) for i in input().split()]
odd = 0
end = 0
result = 0
count = 0

for start in range(n):
    while (odd <= k) and (end<n):
        if s[end] % 2:
            odd += 1
        else:
            count += 1
        if (start == 0) and (end == n):
            result = count
            break
        end += 1
    result = max(result, count)
    if s[start] % 2:
        odd -= 1
    else:
        count -= 1

print(result)

