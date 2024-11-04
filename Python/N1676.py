n = int(input())
a = 1
b = 0

if n == 0:
    a = 1

else:
    for i in range(1,n+1):
        a *= i

li = list(map(int,str(a)))
li.reverse()

for i in range(len(li)):
    if li[i] == 0:
        b += 1
    elif li[i] != 0:
        break

print(b)


