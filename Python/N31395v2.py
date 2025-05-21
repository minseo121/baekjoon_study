import sys
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int, input().split()))
i = 0
j = 0
res = n
data = []
data.append(0)

for a in range(1, n):
    if nums[a] < nums[a-1]:
        data.append(a)
    
for a in range(1, len(data)):
    if data[a] != data[a-1]+1:
        res += (data[a] - data[a-1])

print(res)
#생각을 잘못한듯............................