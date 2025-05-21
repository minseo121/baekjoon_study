import sys

data = sys.stdin.readline().split()
n = int(data[0])
x = int(data[1])
y = int(data[2])
a=list(map(int,sys.stdin.readline().split()))

total_meals = 0
total_remain = 0

for length in a:
    meals, remain = divmod(length,y)
    total_meals += meals
    if remain >= x:
        total_meals+=1
        remain -= x
    total_remain += remain

print(total_meals)
print(total_remain)


