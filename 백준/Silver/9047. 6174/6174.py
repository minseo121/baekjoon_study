t = int(input().strip())
result = 6174

for _ in range(t):
    n = input().strip()
    if len(set(n)) == 1:
        print(-1)
        continue
    if int(n) == result:
        print(0)
        continue
    cnt = 0

    while True:
        n = str(n)
        if len(n) < 4:
            n = '0' * (4 - len(n)) + n
        min_num = int("".join(sorted(n))) 
        max_num = int("".join(sorted(n, reverse=True)))  

        n = max_num - min_num
        cnt += 1
        if n == result:
            print(cnt)
            break