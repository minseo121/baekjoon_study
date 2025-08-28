import sys
import heapq as hq
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    n = int(input())
    min_queue = []
    max_queue = []
    hq.heapify(min_queue)
    hq.heapify(max_queue)
    del_list = {}
    vaild = 0 
    for _ in range(n):
        txt, num = input().rstrip().split()
        num = int(num)
        if txt == "I":
            hq.heappush(min_queue, num)
            hq.heappush(max_queue, -num)
            if num in del_list:
                del_list[num] += 1 
            else:
                del_list[num] = 1

            vaild += 1 
        elif txt == "D":
            if num == -1:
                while min_queue:
                    del_num = hq.heappop(min_queue)
                    if del_num in del_list and del_list[del_num] > 0:
                        del_list[del_num] -= 1 
                        vaild -= 1 
                        break

            elif num == 1:
                while max_queue:
                    del_num = -hq.heappop(max_queue)
                    if del_num in del_list and del_list[del_num] > 0:
                        del_list[del_num] -= 1
                        vaild -= 1 
                        break

    if vaild > 0 : 
        while True:
            min_ = hq.heappop(min_queue)
            if min_ in del_list and del_list[min_] > 0: 
                break
        while True:
            max_ = -hq.heappop(max_queue)
            if max_ in del_list and del_list[max_] > 0: 
                break
        print(max_, min_)
    else:
        print("EMPTY")