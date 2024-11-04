import sys
input = sys.stdin.read
data = input().split()

s = str(data[0])
list(s)

results = [-1 for _ in range(26)]

for i in range(len(s)):
    if s[i] == 'a':
        results[0] += 1
    elif s[i] == 'b':
        results[1] += 1
    elif s[i] == 'c':
        results[2] += 1
    elif s[i] == 'd':
        results[3] += 1
    elif s[i] == 'e':
        results[4] += 1
    elif s[i] == 'f':
        results[5] += 1
    elif s[i] == 'g':
        results[6] += 1
    elif s[i] == 'h':
        results[7] += 1
    elif s[i] == 'i':
        results[8] += 1
    elif s[i] == 'j':
        results[9] += 1
    elif s[i] == 'k':
        results[10] += 1
    elif s[i] == 'l':
        results[11] += 1
    elif s[i] == 'm':
        results[12] += 1
    elif s[i] == 'n':
        results[13] += 1
    elif s[i] == 'o':
        results[14] += 1
    elif s[i] == 'p':
        results[15] += 1
    elif s[i] == 'q':
        results[16] += 1
    elif s[i] == 'r':
        results[17] += 1
    elif s[i] == 's':
        results[18] += 1
    elif s[i] == 't':
        results[19] += 1
    elif s[i] == 'u':
        results[20] += 1
    elif s[i] == 'v':
        results[21] += 1
    elif s[i] == 'w':
        results[22] += 1
    elif s[i] == 'x':
        results[23] += 1
    elif s[i] == 'y':
        results[24] += 1
    elif s[i] == 'z':
        results[25] += 1

sys.stdout.write(" ".join(map(str, results)) + "\n")