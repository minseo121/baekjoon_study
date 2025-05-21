import sys
input = sys.stdin.readline

n = int(input().strip())
for i in range(n):
    a = [['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],[0]*26]
    a2 = [['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']]

    s = input()
    for w in s:
        for j in range(26):
            if a2[0][j] == w:
                w = a2[1][j]
            if a[0][j] == w:
                a[1][j] += 1
    
    num = min(a[1])
    idx = str(i+1)+':'
    if num == 1:
        print('Case',idx,'Pangram!')
    if num == 2:
        print('Case',idx,'Double pangram!!')
    if num == 3:
        print('Case',idx,'Triple pangram!!!')
    if num == 0:
        print('Case',idx,'Not a pangram')
