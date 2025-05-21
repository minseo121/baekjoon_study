import sys
input = sys.stdin.readline

while True:
    num = []
    for i in range(10):
        num.append(i+1)
    while True:
        n = int(input().strip())
        if n == 0:
            break
        ans = input().strip()
        result = 'Stan may be honest'
        if ans == 'right on':
            break
        elif ans == 'too high':
            if n > max(num):
                result = 'Stan is dishonest'
                continue
            if num:
                for i in range(11-n):
                    num.pop()
                    if not num:
                        result = 'Stan is dishonest'
                        break
        elif ans == 'too low':
            if n < min(num):
                result = 'Stan is dishonest'
                continue
            if num:
                num.reverse()
                for i in range(n):
                    num.pop()
                    if not num:
                        result = 'Stan is dishonest'
                        break
                num.reverse()
    if not num:
        result = 'Stan is dishonest'
    if n == 0:
        break
    print(result)
