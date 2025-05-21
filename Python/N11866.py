import sys

n, k = map(int, sys.stdin.readline().split())
data = list(range(1, n + 1)) 
result = []

index = 0
while data:
    index = (index + k - 1) % len(data)  
    result.append(data.pop(index))  

sys.stdout.write("<" + ", ".join(map(str, result)) + ">")
