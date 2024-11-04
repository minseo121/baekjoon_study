def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b) 

import sys
input = sys.stdin.read
data = input().split()
index = 1

n=int(data[0])
for _ in range(n):
    a = int(data[index])
    b = int(data[index+1])
    index += 2
    print(lcm(a,b))