import sys
input = sys.stdin.readline

n = int(input().strip())
member = dict()
for _ in range(n):
    name = input().strip()
    if name in member.keys(): #만약 해당하는 이름이 member의 키들에 있으면~
        member[name] += 1 #1을 추가하고 (중복 체크)
    else: 
        member[name] = 1 #아니면 해당 키값의 value에 1을 넣어라.

for _ in range(n-1): #1명의 배부른 마라토너 말고 다른 이름들이 들어오는 부분 
    name = input().strip()
    if member[name] > 0:
        member[name] -= 1 #들어오는 이름들이 키값인 value의 값이 0보다 클때는 1씩 빼준다.
        #중복체크

for key, values in member.items():
    if values == 1: #value값을 돌면서 찾다가 1인 값을 출력 
        print(key)
        break