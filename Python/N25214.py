import sys

n = int(input())
a = []
data = sys.stdin.readline().split()
print(data)
result = []

for i in range(n):
    a.append(int(data[i]))
    print(a)
    mi = min(a)
    ma = min(a)
    for j in range(i):
        if mi == int(a[j]) and i > j:
            for l in range(j,i):
                if ma < a[l]:
                    ma = a[l] #최대값 찾고
                    print('여길 지나고 있나요?', ma, a[l])
        else:
            ma = max(a)
            print('else문은 잘 들어감?')
    print('min', mi , 'max', ma)
    
    result.append(int(ma)-int(mi))

for i in range(n):
    print(result[i])
