def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b) 

import sys
input = sys.stdin.read
data = input().split()

a = int(data[0])
b = int(data[1])

print(gcd(a, b), lcm(a, b))
