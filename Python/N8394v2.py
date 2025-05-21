import sys
input = sys.stdin.readline

n = int(input().strip())

result = [0]*(n)
result[0]= 2
result[1] = 3

for i in range(2, n-1):
    result[i] = (result[i-2]+result[i-1])%10

print(result[n-2])