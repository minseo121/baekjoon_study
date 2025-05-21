import sys
input = sys.stdin.readline

word = input().strip()
n = len(word)
nums = (n-1)*4+5
maps = [['.']*nums for _ in range(5)]

for i in range(n):
    if i == 0:
        maps[0][2], maps[1][1], maps[1][3], maps[2][0], maps[2][4], maps[3][1], maps[3][3], maps[4][2]= '#','#','#','#','#','#','#','#'
        maps[2][2] = word[i]
    elif (i+1)%3 != 0:
        maps[0][4*i+2], maps[1][4*i+1], maps[1][4*i+3], maps[2][4*i+4], maps[3][4*i+1], maps[3][4*i+3], maps[4][4*i+2]= '#','#','#','#','#','#','#'
        maps[2][4*i+2] = word[i]
        if maps[2][4*i] == '*':
            continue
    else:
        maps[0][4*i+2], maps[1][4*i+1], maps[1][4*i+3], maps[2][4*i+4], maps[3][4*i+1], maps[3][4*i+3], maps[4][4*i+2]= '*','*','*','*','*','*','*'
        maps[2][4*i+2] = word[i]
        if maps[2][4*i] == '#':
            maps[2][4*i] = '*'

for i in maps:
    print(''.join(i))
