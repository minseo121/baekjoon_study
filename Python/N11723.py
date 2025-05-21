import sys

m = int(input())
s = set()

for i in range(m):
    data = sys.stdin.readline().strip().split()
    a = (data[0])

    if len(data) == 1:
        if a == 'all':
            s = set([i for i in range(1,21)])
        else:
            s = set()
        continue

    else: 
        if a == 'add':
            s.add(int(data[1]))
        elif a == 'remove':
            s.discard(int(data[1]))
        elif a == 'check':
            if int(data[1]) in s:
                print(1)
            else:
                print(0)
        elif a == 'toggle':
            if int(data[1]) in s:
                s.discard(int(data[1]))
            else:
                s.add(int(data[1]))
        else:
            print("다시 입력해주세요!")
