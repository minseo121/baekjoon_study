import sys

def gcd(num1, num2):
  while(True):
    r= num2 % num1
    if r == 0:
      return num1
    num2 = num1; num1 = r

input = sys.stdin.readline

for _ in range(int(input())):
  a = list(map(int,input().split()))
  n, nums, r = a[0], a[1:], 0

  for i in range(n-1):
    for j in range(i+1,n):
      r += gcd(nums[i], nums[j])
  print(int(r))