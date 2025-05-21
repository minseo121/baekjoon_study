n = int(input())

end = 666
cnt = 0

while True:
    if '666' in str(end):
        cnt += 1
        if cnt == n:
            break
    end += 1

print(end)