import sys
import math

def sosu(num):
    lists = [True for i in range(num + 1)] 
    lists[0] = lists[1] = False
    for i in range(2, int(math.sqrt(num)) + 1):
        if lists[i] == True:
            for j in range(i*i, num+1, i):
                lists[j] = False
    return lists

input = sys.stdin.read
data = input().split()

max_num = max(int(num) for num in data if num.isdigit())
sosus = sosu(max_num)
results = []

for i in range(len(data)):
    num = int(data[i])
    if num == 0:
        break
    
    found = False
    for a in range(3, num // 2 + 1, 2):
        b = num - a
        if sosus[a] and sosus[b]:
            results.append(f"{num} = {a} + {b}")
            found = True
            break
    if not found:
        results.append("Goldbach's conjecture is wrong.")

sys.stdout.write('\n'.join(results))
