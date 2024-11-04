import sys
input = sys.stdin.read

data = input().split()
n = int(data[0])
numbers = list(map(int, data[1:]))

result = [-1] * n
stack = []

for i in range(n):
    while stack and numbers[stack[-1]] < numbers[i]:
        result[stack.pop()] = numbers[i]
    stack.append(i)

sys.stdout.write(" ".join(map(str, result)) + "\n")
