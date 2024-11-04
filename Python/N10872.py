n = int(input())
a = 1

if n == 0:
    a = 1

else:
    for i in range(1,n+1):
        a *= i

print(a)

