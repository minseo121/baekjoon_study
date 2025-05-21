import sys

n = input()
s = sys.stdin.readline().strip()
print(s)
last = s[-1]

jong = ['r', 's', 'e', 'f', 'a', 'q', 't','d', 'w', 'c', 'z', 'x','v','g']

if last in jong:
    print(1)
else:
    print(0)