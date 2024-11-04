import sys

prime = []
checks = [0] * 1000001
checks[0] = 1
checks[1] = 1

for i in range(2,1000001):
  if checks[i] == 0: 
    prime.append(i) #소수인 값들만 남음. prime에 넣어줌
    for j in range(2*i, 1000001, i):
      checks[j] = 1 #소수가 아닌 값들을 다 1로 바꾸기

T = int(input())

for _ in range(T):
  count = 0
  n = int(input())
  for i in prime:
    if i >= n :
      break
    if not checks[n-i] and i <= n-i:
      count += 1
  print(count)
