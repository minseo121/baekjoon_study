import sys

result = []

while True:
    data=sys.stdin.readline().strip()

    if data == "0":
        break

    ls = list(data)
    sls = []

    if len(ls) % 2 != 0:
        i = len(ls)//2
        for j in range(i):
            sls.append(ls.pop())
        ls.pop()
        if ls == sls:
            result.append('Yes')
        else:
            result.append('No')
    elif len(ls) % 2 == 0:
        i = len(ls)//2
        for _ in range(i):
            sls.append(ls.pop())
        if ls == sls:
            result.append('Yes')
        else:
            result.append('No')
    else:
        break

sys.stdout.write("\n".join(map(str, result))+"\n")