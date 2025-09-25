import sys
input = sys.stdin.readline

t = int(input().strip())
list = ["VVV딸기","VV딸기V","VV딸기딸기","V딸기VV","V딸기V딸기","V딸기딸기V","V딸기딸기딸기","딸기VVV","딸기VV딸기","딸기V딸기V","딸기V딸기딸기","딸기딸기VV","딸기딸기V딸기","딸기딸기딸기V","딸기딸기딸기딸기"]

while t:
    n = int(input().strip())
    k = (n - 1) % 28
    if k <= 14:
        idx = k
    else:
        idx = 28 - k
    print(list[idx])
    t -= 1

    