import sys

count = sys.stdin.readline().split()
n = int(count[0])
m = int(count[1])

s1 = set(sys.stdin.readline().strip() for _ in range(n))
s2 = set(sys.stdin.readline().strip() for _ in range(m))

result = sorted(s1 & s2) #배열에 정렬

print(len(result))
for name in result:
    print(name)