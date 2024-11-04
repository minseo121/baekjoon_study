import queue
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
que = queue.Queue()
index = 1

results = []

for i in range(n):
    a = data[index]
    
    if a == "push":
        b = int(data[index + 1])
        que.put(b)
        index += 2
    elif a == "pop":
        if not que.empty():
            results.append(que.get())
        else:
            results.append(-1)
        index += 1
    elif a == "size":
        results.append(que.qsize())
        index += 1
    elif a == "empty":
        if que.empty():
            results.append(1)
        else:
            results.append(0)
        index += 1
    elif a == "front":
        if not que.empty():
            results.append(que.queue[0])
        else:
            results.append(-1)
        index += 1
    elif a == "back":
        if not que.empty():
            results.append(que.queue[-1])
        else:
            results.append(-1)
        index += 1
    else:
        results.append("잘못된입력")
        index += 1

sys.stdout.write("\n".join(map(str, results)) + "\n")
