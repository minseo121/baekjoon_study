import sys
input = sys.stdin.readline

n = int(input().strip())

a = 2
b = 3

for i in range(2, n-1):
    if i % 2 == 0:
        a = (a+b)%10
    else:
        b = (a+b)%10

if (n-2) % 2 == 0:
    print(a)
else:
    print(b)