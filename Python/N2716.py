import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    op = sys.stdin.readline()

    maxdepth = 0
    tree = []
    for o in op:
        if o == "]":
            maxdepth = max(len(tree),maxdepth)
            tree.pop() #열린 괄호 제거
        else:
            tree.append("[")
    print(2**maxdepth)
