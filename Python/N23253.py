import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = []

for _ in range(m):
    num = int(input())
    d.append(list(map(int, input().split())))

want = 1
idx = 0

while d:
    if not d[idx]:
        if idx != n:
            idx += 1
            if idx == n:
                break
        else:
            break
    else:
        book_num = d[idx].pop()
        if book_num == want:
            want += 1
            idx = 0
            if want == n:
                break
        else:
            d[idx].append(book_num)
            idx += 1
            if idx == m:
                break

if want == n:
    print("Yes")
else:
    print("No")

