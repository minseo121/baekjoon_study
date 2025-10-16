import sys
input = sys.stdin.readline

n = int(input().strip())
nums = {}

nums[0] = 0
nums[1] = 1
nums[2] = 1

def dp(i):
    if not i in nums:
        if i % 2 == 0:
            nums[i] = (dp(i//2)*(dp(i//2)+2*dp(i//2 - 1)))%1000000007
        else:
            nums[i] = (dp(i//2)**2 + dp(i//2+1)**2)%1000000007
    return nums[i]

print(dp(n))