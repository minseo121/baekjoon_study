import sys

data = sys.stdin.readline().split()
a = int(data[0])
b = int(data[1])
v = int(data[2])
day = 0

if (v-b)%(a-b) == 0:
    day = (v-b)//(a-b)
else:
    day = (v-b)//(a-b) + 1

sys.stdout.write(str(day))