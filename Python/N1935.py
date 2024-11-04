import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])  
num = [0] * n
index = 2

for i in range(n):
    num[i] = int(data[index])
    index += 1

li = list(data[1]) 

for i in range(len(li)):
    if 'A' <= li[i] <= 'Z':
        li[i] = num[ord(li[i]) - 65] 

stack = []

for i in range(len(li)):
    if isinstance(li[i], int): 
        stack.append(li[i])
    else: 
        b = stack.pop()
        a = stack.pop()
        if li[i] == '+':
            stack.append(a + b)
        elif li[i] == '-':
            stack.append(a - b)
        elif li[i] == '*':
            stack.append(a * b)
        elif li[i] == '/':
            stack.append(a / b) 

print(f"{stack[0]:.2f}")  
