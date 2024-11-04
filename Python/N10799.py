import sys
input = sys.stdin.read
data = input().strip()

stack = []
n = 0

for i in range(len(data)):
    if data[i] == '(':
        stack.append('(')
    elif data[i] == ')':
        if data[i-1] == '(':  
            stack.pop()
            n += len(stack)
        else:  
            stack.pop()
            n += 1

print(n)
