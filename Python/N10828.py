import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
stack = []
index = 1

results = []

for i in range(n):
    a = data[index]
    
    if a == "push":
        b = int(data[index + 1])
        stack.append(b)
        index += 2
    elif a == "pop":
        if stack:
            results.append(stack.pop())
        else:
            results.append(-1)
        index += 1
    elif a == "size":
        results.append(len(stack))
        index += 1
    elif a == "empty":
        if not stack:
            results.append(1)
        else:
            results.append(0)
        index += 1
    elif a == "top":
        if not stack:
            results.append(-1)
        else:
            results.append(stack[-1])
        index += 1
    else:
        results.append("잘못된입력")
        index += 1

sys.stdout.write("\n".join(map(str, results)) + "\n")
