def found_nemo(y, x, n):
    color = paper[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            if color != paper[i][j]:
                m = n//2
                found_nemo(y, x, m)
                found_nemo(y, x+m, m)
                found_nemo(y+m, x, m)
                found_nemo(y+m, x+m, m)
                return
    if color == 0:
        result[0] += 1
    else:
        result[1] += 1
import sys
input = sys.stdin.readline

n = int(input().strip())
paper = [list(map(int, input().split())) for _ in range(n)]
result = [0,0]
found_nemo(0, 0, n)
print(result[0], "\n", result[1],sep='')




