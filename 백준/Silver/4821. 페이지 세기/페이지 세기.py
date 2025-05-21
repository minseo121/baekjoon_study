import sys

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    else:
        data = sys.stdin.readline().rstrip().split(',')
        printed_page = [0]*(n+1)
        pages = 0

        for page_num in data:
            if '-' in page_num:
                low, high = map(int, page_num.split('-'))
                if high > n:
                    high = n
                if low <= high:
                    for i in range(low, high+1):
                        if printed_page[i] == 0:
                            printed_page[i] += 1
                elif low>high:
                    continue
            else:
                one_page = int(page_num)
                if one_page <= n:
                    if printed_page[one_page] == 0:
                        printed_page[one_page] += 1

    for i in range(1, n+1):
        pages += printed_page[i]
    sys.stdout.write(str(pages)+"\n")
