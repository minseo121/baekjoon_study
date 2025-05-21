import sys
import math
input = sys.stdin.readline

def sosu(n):
    li = [1] * (n + 1)
    for i in range(2, int(n**0.5) + 1):
        if li[i]:  # li[i]가 1인 애들만 들어감
            for j in range(i + i, n + 1, i):  # i의 배수 값들을 확인하는 for문
                li[j] = 0  # 그리고 그것에 해당하는 값들은 0으로 바꿔줌
    p = [i for i in range(2, n + 1) if li[i]]  # li[i]가 1인 값들을 p라는 배열에 넣어줌
    return p

while True:
    n = input().strip()
    if n == '0':
        break
    else:
        num = []
        if len(n) == 1:
            # 고대로 출력
            print(n)
        else:
            for i in range(len(n)):
                for j in range(i + 1, len(n) + 1): 
                    a = n[:i]  # 앞부분 자름
                    b = n[i:j]  # 중간 부분 자름
                    c = n[j:]  # 뒷부분 자름

                    if a and int(a) not in num:
                        num.append(int(a))
                    if b and int(b) not in num:
                        num.append(int(b))
                    if c and int(c) not in num:
                        num.append(int(c))

        num.sort()
        p = sosu(100000)  # 소수 리스트 생성
        result = 2
        for prime in p:
            if prime in num:  # 소수 중에서 num에 있는 것 찾기
                result = prime
        print(result)
