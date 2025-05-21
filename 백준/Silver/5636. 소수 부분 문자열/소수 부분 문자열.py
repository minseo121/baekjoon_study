def sosu(n):
    li = [1]*(n+1)
    for i in range(2, int(n**0.5)+1):
        if li[i]: #li[i]가 1인 애들만 들어감
            for j in range(i+i, n+1, i): #i의 배수 값들을 확인하는 for문. [2i, 3i, 4i...]로 진행
                li[j] = 0 #그리고 그것에 해당하는 값들은 0으로 바꿔주기
    p = [i for i in range(2, n+1) if li[i]] #li[i]가 1인 값들을 p라는 배열에 넣어줌 (그러니 위 과정으로 소수인 값들만 현재 1임)
    return p

while True:
    s = input()
    if s == '0':
        break
    p = sosu(100000) #문제에서 지정한 범위까지 그냥 싹 구해놓고
    result = 2
    for n in p: #p에 있는 값들을 하나씩 골라서
        if str(n) in s: #만약 그 n의 값이 string 형태로 들어온 s와 같다면
            result = n #result에 저장
    print(result) #마지막에 저장된 값이 가장 크므로 출력
    