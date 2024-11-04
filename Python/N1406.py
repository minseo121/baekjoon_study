import sys
input = sys.stdin.read

data = input().split()
lis = list(data[0])  
n = int(data[1]) 

stack = lis[:]
pop = []
index = 2  

for _ in range(n):
    command = data[index]
    if command == "L":
        if stack:
            pop.append(stack.pop())
        index += 1
    elif command == "D":
        if pop:
            stack.append(pop.pop())
        index += 1
    elif command == "B":
        if stack:
            stack.pop()
        index += 1
    elif command == "P":
        char = data[index + 1]
        stack.append(char)
        index += 2
    else:
        index += 1

while pop:
    stack.append(pop.pop())

sys.stdout.write("".join(stack) + "\n")
