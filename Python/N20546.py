import sys
input = sys.stdin.readline

m = int(input().strip())
graph = list(map(int, input().split()))
bnp = m
timing = m
count = 0

for i in range(len(graph)-1):
    if bnp >= graph[i]:
        num = bnp // graph[i]
        bnp -= num*graph[i]
        count += num

bnp = bnp + (graph[len(graph)-1]*count)

good = 0
count = 0
for i in range(len(graph)-1):
    if i != 0:
        if graph[i-1] > graph[i]:
            if good >= 0:
                good += 1
            else:
                good = 1
        elif graph[i-1] < graph[i]:
            if good <= 0:
                good -= 1
            else:
                good = -1
        else:
            good = 0

    if good == 3:
        if timing >= graph[i]:
            num = timing // graph[i]
            timing -= num*graph[i]
            count += num
            good = 2

    if good == -3 and count != 0:
        timing += graph[i]*count
        good = -2
        count = 0

timing = timing + (graph[len(graph)-1])*count

if bnp == timing:
    print("SAMESAME")
elif bnp > timing:
    print("BNP")
else:
    print("TIMING")