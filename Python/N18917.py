import sys
input = sys.stdin.readline

m = int(input().strip())
a = []
a.append(0)
sum = 0

for _ in range(m):
    data = list(map(int, input().split()))
    if data[0] == 1:
        a.append(data[1])
        sum += data[1]
    elif data[0] == 2:
        a.remove(data[1])
        sum -= data[1]
    elif data[0] == 3:
        print(sum)
    else: #data[0] == 4
        print(sum.__xor__)
            

