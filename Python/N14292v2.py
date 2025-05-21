import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int, input().split()))
deq = deque()
deq2 = deque()
idx = 0
result = 0
count = 0

for i in range(1, n):
    deq.append(nums[i])

while deq:
    num = deq.popleft()
    result += nums[idx] * num
    count += 1
    if count > 1:
        deq2.append(num)
        print('deq2', deq2)
    if count == n-idx-1:
        deq = deq2
        deq2.clear()

print(result)

