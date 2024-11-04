import sys

def gcd(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1

input = sys.stdin.readline
data = input().split()

ls = []
n = int(data[0])
s = int(data[1])
a = list(map(int, input().split()))

for i in range(n):
    ls.append(abs(s - a[i]))  

r = ls[0]
for i in range(1, len(ls)):
    r = gcd(r, ls[i])

print(r)
