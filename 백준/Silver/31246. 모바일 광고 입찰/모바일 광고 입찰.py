import sys
input = sys.stdin.readline
n, k = map(int, input().split())
price = []

for i in range(0, n):
    a, b = map(int, input().split())
    if a > b:
        price.append(0)
    else:
        price.append(b-a)
    

price.sort()
print(price[k-1])