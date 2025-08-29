import sys
input = sys.stdin.readline

import sys
x = list(input().strip())
M = list(input().strip())
m = len(M)
stack = []
for i in x:
    stack.append(i)
    if stack[len(stack)-m:len(stack)] == M: 
        for _ in range(m): 
            stack.pop() 
if stack:
    print(*stack, sep='')
else:
    print("FRULA")