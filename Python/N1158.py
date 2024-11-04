import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])

queue = list(range(1, n + 1))
results = []
index = 0

while queue:
    index = (index + k - 1) % len(queue)
    results.append(queue.pop(index))

sys.stdout.write("<" + ", ".join(map(str, results)) + ">")
