import sys

n = input().split('-')

num = []

for i in n:
    sum = 0
    data = i.split('+')
    for j in data:
        sum += int(j)
    num.append(sum)

first = num[0]
for i in range(1, len(num)):
    first -= num[i]

print(first)
