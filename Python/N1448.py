import sys

n = int(sys.stdin.readline().strip())
num = []
sum = []

if n < 3:
    print(-1)

else:
    for i in range(n):
        num.append(int(sys.stdin.readline().strip()))

    for i in range(n):
        for j in range(n):
            if i!=j:
                for l in range(n):
                    if l != i and l != j:
                        ex = []
                        ex.append(num[i])
                        ex.append(num[j])
                        ex.append(num[l])
                        ex.sort()
                        m = ex.pop()
                        b = ex.pop()
                        c = ex.pop()
                        if m*m < b*b+c*c:
                            sum.append(m+b+c)
                        else:
                            sum.append(-1)
sys.stdout.write(str(max(sum)))


