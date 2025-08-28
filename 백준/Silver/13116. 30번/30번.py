import sys
input = sys.stdin.readline

t = int(input().strip())

while t:
    a, b = map(int, input().rsplit())
    while True:
        if a == b:
            print(10*a)
            break
        if a > b :
            a //= 2
        if b > a :
            b //= 2 
    t -= 1
