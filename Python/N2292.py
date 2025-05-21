import sys

n = int(sys.stdin.readline().strip())
nbox = 1
count = 1

while n > nbox:
    nbox += 6*count
    count += 1

print(count)