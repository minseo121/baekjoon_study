import sys
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().split()))
m = int(input().strip())
b = list(map(int, input().split()))

common = set(a)&set(b)

if not common:
    print(0)
    exit()

result = []
while common:
    max_val = max(common)
    result.append(max_val)

    idx1 = a.index(max_val)
    idx2 = b.index(max_val)
    a = a[idx1 + 1:]
    b = b[idx2 + 1:]

    common = set(a) & set(b)

print(len(result))
print(' '.join(map(str, result)))