import sys
from fractions import Fraction
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().split()))
sum = 0

for i in range(n):
    sum += Fraction(1, a[i])

result = str(Fraction(1, sum))

if '/' not in result:
    print(result+'/1')
else:
    print(result)