import sys
input = sys.stdin.readline

n = int(input())
w1 = input()
w2 = input()
first = False
second = False
third = False
a = [['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
a2 = [['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        
for i in range(n):
    for j in range(26):
        if w1[i] == a[0][j]:
            a[1][j] += 1
        if w2[i] == a2[0][j]:
            a2[1][j] += 1
if a2[1] == a[1]:
    first=True #첫번째 조건 만족 (알파벳 개수가 같은지만 확인)

if w1[0] == w2[0] and w1[n-1] == w2[n-1]:
    second = True #두번째 조건 만족

wb1 =[]
wb2=[]
for i in range(n):
    wb1.append(w1[i])
    wb2.append(w2[i])

i = 0
j = 0
while len(wb1) != i:
    if wb1[i] in ['a','e','i','o','u']:
        wb1.pop(i)
    else:
        i += 1
while len(wb2) != j:
    if wb2[j] in ['a','e','i','o','u']:
        wb2.pop(j)
    else:
        j += 1
if wb1 == wb2:
    third = True
    #세번째 조건 만족

if first and second and third:
    print('YES')
else:
    print('NO')