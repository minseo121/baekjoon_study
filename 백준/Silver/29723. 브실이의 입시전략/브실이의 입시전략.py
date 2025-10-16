import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
score = {}
total_score = 0

for _ in range(n):
    data = input().split()
    num = int(data[1])
    score[data[0]] = num

for _ in range(k):
    data = input().strip()
    total_score += score[data]
    del score[data]

pick = m-k
if pick == 0:
    print(total_score, total_score)
else:
    nums = list(score.values())
    nums.sort()
    low = sum(nums[:pick])
    high = sum(nums[-pick:])
    print(total_score+low, total_score+high)