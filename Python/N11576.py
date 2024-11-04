a, b = map(int,input().split())
num = int(input())
c = list(map(int,input().split()))[::-1]
x = 0
result = []

for i in range(len(c)):
    x += c[i] * (a**i)

while x != 0:
    result.append(x%b)
    x//=b
print(" ".join(map(str,result[::-1])))