def found(array, target, start, end):
    result = 0 
    while start <= end:
        mid = (start + end) // 2
        sum = 0
        for height in array:
            if height > mid: 
                sum += height - mid
        if sum >= target: 
            result = mid  
            start = mid + 1 
        else:
            end = mid - 1  
    return result

import sys
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split()))
tree = list(map(int, input().split()))

tree.sort()
result = found(tree, m, 0, tree[-1])

print(result)
