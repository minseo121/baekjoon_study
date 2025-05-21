import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    wear_data = {}
    for i in range(n):
        wearname, type = map(str, input().split())
        if type in wear_data:
            wear_data[type] += 1
        else:
            wear_data[type] = 1
    cnt = 1
    for i in wear_data:
        cnt *= (wear_data[i]+1)

    print(cnt-1)

    
    