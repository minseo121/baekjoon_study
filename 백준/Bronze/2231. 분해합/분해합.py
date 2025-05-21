n = int(input())
m = 0

while True:
    if m >= n:
            m = 0
            break
    num = sum((map(int, str(m))))
    if n == m + num:
        break
    else:
        m += 1

print(m)
