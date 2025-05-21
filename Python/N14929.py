import sys
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int, input().split()))
temp = sum(nums)
result = 0

for i in range(n):
    temp -= nums[i]
    result += temp * nums[i]

print(result)