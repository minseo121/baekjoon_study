from collections import deque
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
deq = deque()
index = 1

results = []

for i in range(n):
    a = data[index]

    if a == "push_front":
        b = int(data[index+1])
        deq.appendleft(b)
        index += 2
    elif a == "push_back":
        b = int(data[index+1])
        deq.append(b)
        index += 2
    elif a == "pop_front":
        if deq:
            results.append(deq.popleft())
        else :
            results.append(-1)
        index += 1
    elif a == "pop_back":
        if deq:
            results.append(deq.pop())
        else :
            results.append(-1)
        index += 1
    elif a == "size":
        results.append(len(deq))
        index += 1
    elif a == "empty":
        if not deq:
            results.append(1)
        else:
            results.append(0)
        index += 1
    elif a == "front":
        if not deq:
            results.append(-1)
        else:
            results.append(deq[0])
        index += 1
    elif a == "back":
        if not deq:
            results.append(-1)
        else:
            results.append(deq[-1])
        index += 1
    else:
        results.append("잘못된입력")
        index += 1

sys.stdout.write("\n".join(map(str, results)) + "\n")
