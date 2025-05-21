import sys
inpur = sys.stdin.readline

def dot_min(a): #선분 안에서 가장 작은 점의 값
    start = 0
    end = n-1
    while start <= end:
        mid = (start+end)//2
        if dot[mid] < a: #만약 dot[mid]값이 제일 작은 선분의 점의 값보다 작다면
            start = mid + 1 #mid에다가 +1 
        else: #크다면
            end = mid - 1 #start랑 end가 만날때까지 확인하면서 제일 작은 값 찾기
    
    return end + 1 #마지막으로 찾은 값이 -1이 됐을 거기 때문에 +1

def dot_max(b): #선분 안에서 가장 큰 점의 값
    start = 0 #위와 유사한 과정
    end = n-1
    while start <= end:
        mid = (start+end)//2
        if dot[mid] > b:
            end = mid - 1
        else:
            start = mid + 1
    
    return end 


n, m = map(int, input().split())
dot = list(map(int, input().split()))

dot.sort() #이분탐색을 위해 수 정렬 해놓기

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(dot_max(b) - dot_min(a) + 1) 
