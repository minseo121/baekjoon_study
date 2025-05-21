import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(set(map(int, input().split()))) 
res = []

def bt(start, depth):
    if depth == m:
        print(*res)
        return
    for i in range(start, len(nums)):  # 현재 숫자부터 시작 (비내림차순 보장)
        res.append(nums[i])
        bt(i, depth + 1)  # 같은 숫자를 다시 사용할 수 있도록 i 전달
        res.pop()

bt(0, 0)
