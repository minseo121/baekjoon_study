n=int(input())
res=''

if n==0:
  print(0)
  exit
while n!=0:
  if n%(-2) !=0:
    res += '1'
    n = n//(-2)+1
  else:
    res+= '0'
    n = n//(-2)

print(res[::-1])