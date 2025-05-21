import sys
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int, input().split()))
res = [1] * n
result = 0

for i in range(1,n):
    if nums[i] > nums[i-1]:
        res[i] = res[i-1]+1

for i in range(n):
    result += res[i]

print(result)
        
