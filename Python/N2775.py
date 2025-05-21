import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    k = int(sys.stdin.readline().strip())  
    n = int(sys.stdin.readline().strip()) 

    apt = [[0] * (n + 1) for _ in range(k + 1)] 

    for j in range(1, n + 1):
        apt[0][j] = j

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            if j == 1:
                apt[i][j] = 1  
            else:
                apt[i][j] = apt[i][j - 1] + apt[i - 1][j]
                
    sys.stdout.write(str(apt[k][n]) + "\n")
