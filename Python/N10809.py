import sys
input = sys.stdin.read
data = input().split()

s = str(data[0])
list(s)

results = [-1 for _ in range(26)]

for i in range(len(s)):
    if s[i] == 'a':
       if results[0] != -1:
           continue
       else :
           results[0] = i
    elif s[i] == 'b':
        if results[1] != -1:
           continue
        else :
           results[1] = i
    elif s[i] == 'c':
        if results[2] != -1:
           continue
        else :
           results[2] = i
    elif s[i] == 'd':
        if results[3] != -1:
           continue
        else :
           results[3] = i
    elif s[i] == 'e':
        if results[4] != -1:
           continue
        else :
           results[4] = i
    elif s[i] == 'f':
        if results[5] != -1:
           continue
        else :
           results[5] = i
    elif s[i] == 'g':
        if results[6] != -1:
           continue
        else :
           results[6] = i
    elif s[i] == 'h':
        if results[7] != -1:
           continue
        else :
           results[7] = i
    elif s[i] == 'i':
        if results[8] != -1:
           continue
        else :
           results[8] = i
    elif s[i] == 'j':
        if results[9] != -1:
           continue
        else :
           results[9] = i
    elif s[i] == 'k':
        if results[10] != -1:
           continue
        else :
           results[10] = i
    elif s[i] == 'l':
        if results[11] != -1:
           continue
        else :
           results[11] = i
    elif s[i] == 'm':
        if results[12] != -1:
           continue
        else :
           results[12] = i
    elif s[i] == 'n':
        if results[13] != -1:
           continue
        else :
           results[13] = i
    elif s[i] == 'o':
        if results[14] != -1:
           continue
        else :
           results[14] = i
    elif s[i] == 'p':
        if results[15] != -1:
           continue
        else :
           results[15] = i
    elif s[i] == 'q':
        if results[16] != -1:
           continue
        else :
           results[16] = i
    elif s[i] == 'r':
        if results[17] != -1:
           continue
        else :
           results[17] = i
    elif s[i] == 's':
        if results[18] != -1:
           continue
        else :
           results[18] = i
    elif s[i] == 't':
        if results[19] != -1:
           continue
        else :
           results[19] = i
    elif s[i] == 'u':
        if results[20] != -1:
           continue
        else :
           results[20] = i
    elif s[i] == 'v':
        if results[21] != -1:
           continue
        else :
           results[21] = i
    elif s[i] == 'w':
        if results[22] != -1:
           continue
        else :
           results[22] = i
    elif s[i] == 'x':
        if results[23] != -1:
           continue
        else :
           results[23] = i
    elif s[i] == 'y':
        if results[24] != -1:
           continue
        else :
           results[24] = i
    elif s[i] == 'z':
        if results[25] != -1:
           continue
        else :
           results[25] = i
sys.stdout.write(" ".join(map(str, results)) + "\n")