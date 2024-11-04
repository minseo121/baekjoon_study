import sys
input = sys.stdin.read
data = input().split(' ')

a = int(data[0])
b = int(data[1])
c = int(data[2])

results = []

results.append((a+b)%c)
results.append(((a%c)+(b%c))%c)
results.append((a*b)%c)
results.append(((a%c)*(b%c))%c)

sys.stdout.write("\n".join(map(str,results))+"\n")
