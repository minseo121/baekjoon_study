import sys
input = sys.stdin.readline

s = []
n = int(input())

while n > 0:
    s.append(n%2)
    n //= 2

sum = 0
for i in range(len(s)):
    if s[i] == 1:
        sum += 3**i

print(sum)