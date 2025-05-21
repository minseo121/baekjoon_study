import sys
input = sys.stdin.readline

t = int(input().strip())
while t:
    n = int(input().strip())
    nums = set(map(int, input().split()))
    m = int(input().strip())
    mnums = list(map(int, input().split()))

    setMnums = set(mnums)
    ans = set.intersection(nums, setMnums)

    for i in range(m):
        if mnums[i] in ans:
            print(1)
        else:
            print(0)
    t -= 1