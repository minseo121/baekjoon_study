import sys
input = sys.stdin.readline

n = int(input().strip())
time = []
end = 0
start = 0
result = 0

for _ in range(n):
    time.append(list(map(int, input().rstrip().split())))

time.sort(key=lambda x: (x[1], x[0]))

for newStart, newEnd in time:
    if end <= newStart:
        result += 1
        end = newEnd

print(result)