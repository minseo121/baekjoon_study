import sys
input = sys.stdin.read
data = input().splitlines()

a = 0 #대문자
b = 0 #소문자
c = 0 #공백
d = 0 #숫자

for i in range(len(data)):
    li = list(data[i])
    for j in range(len(data[i])):
        if 'A' <= li[j] <= 'Z':
            a += 1
        elif 'a' <= li[j] <= 'z':
            b += 1
        elif li[j].isdigit():
            d += 1
        elif li[j] == ' ':
            c += 1
    print(f"{b} {a} {d} {c}")
    a=0
    b=0
    c=0
    d=0
