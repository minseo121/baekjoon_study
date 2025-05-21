import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = list(map(int, input().split()))
s.sort()
ans = []

def dfs(start):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(0, n):
        if s[i] not in ans:
            ans.append(s[i])
            dfs(i+1)
            ans.pop()

dfs(0)