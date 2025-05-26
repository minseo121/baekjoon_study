import sys
input = sys.stdin.readline

susik = input().strip()
giho = ['+','-','*','/']
num = []
for i in susik:
    if i not in giho:
        num.append(int(i))
    else:
        second = num.pop()
        first = num.pop()
        if i == '+':
            num.append(first+second)
        if i == '-':
            num.append(first-second)
        if i == '*':
            num.append(first*second)
        if i == '/':
            num.append(first//second)

print(num.pop())
