import sys
input = sys.stdin.readline

n = int(input().strip())
a, b = map(int, input().split())
c = int(input().strip())
topping = []

for _ in range(n):
    topping.append(int(input().strip()))

topping.sort()

good = c//a
good_eat = c
good_cost = a
for i in range(n-1, -1, -1):
    if (good_eat+topping[i])//(good_cost+b) >= good:
        good = (good_eat+topping[i])//(good_cost+b)
        good_eat += topping[i]
        good_cost += b
    else: 
        break

print(good)