import sys
input = sys.stdin.readline

m,s = map(int, input().split(':'))

cnt = 1
#조리 시작~ 미리 눌러놓고
cnt += (m//10+m%10)

if s >= 30:
    cnt += (s-30)//10
else:
    cnt += s//10

print(cnt)