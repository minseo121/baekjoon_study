import sys
input = sys.stdin.read
data = input().strip()

lines = data.split('\n')
n = int(lines[0])

results=[]

for i in range(1, n + 1):
    if i < len(lines):
        a = lines[i]
        a2 = a.split(' ')
        l = len(a2)
        for j in range(l):
            b = str(a2[j])
            n_list = list(b)
            n_list.reverse()
            b = ''.join(n_list)
            results.append(b + " ")
        results.append("\n")

sys.stdout.write("".join(map(str, results)) + "\n")
