import sys

n = int(sys.stdin.readline().strip())
v = sys.stdin.readline().split()
v.reverse()
sum = 0
a = 0

for i in range(n):
    if i == 0:
        a = 1
        sum += 1
    else:
        a = min(a+1, int(v[i]))
        sum += a


print(sum)





# v[n-1] = 1 

# for i in range(n): 
#     if i != n-1:
#         m = int(v[i])
#         for j in range(n-i):
#             if m > int(v[i+j])+j:
#                 m = int(v[i+j])+j
#         sum += m
#     else:
#         sum+=1

#sys.stdout.write(sum)