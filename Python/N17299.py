import sys
input = sys.stdin.read

data = input().split()
n = int(data[0])
numbers = list(map(int, data[1:]))

count = [0] * 1000001
result = [-1] * n
stack = []

for i in numbers:
    count[i] += 1

for i in range(n):
    while stack and count[numbers[stack[-1]]] < count[numbers[i]]:
        result[stack.pop()] = numbers[i]
    stack.append(i)

sys.stdout.write(" ".join(map(str, result)) + "\n")
