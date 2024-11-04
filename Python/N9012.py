import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
results = []
sum = 0

for i in range(1, n+1):
    l = len(data[i])
    a = list(data[i])
    for j in range(l):
        b = str(a[j])
        if b == "(" :
            sum += 1
        elif b == ")" :
            sum -= 1
        if sum < 0:
            results.append("NO")
            break
    if sum == 0:
        results.append("YES")
    elif sum > 0:
        results.append("NO")
    sum = 0

sys.stdout.write("\n".join(map(str, results)) + "\n")