n = int(input())
data = [0]*11
data[1] = 1
data[2] = 2
data[3] = 4

for a in range(n):
    num = int(input())
    for i in range(4, num+1):
        data[i] = data[i-1] + data[i-2] + data[i-3]
    print(data[num])


