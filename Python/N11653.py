def sosu(n):
  data=[]
  i = 2
  while i<=n:
    if n%i ==0:
      data.append(i)
      n = n//i
    else:
      i = i+1
  return data

n = int(input())
data = sosu(n)
print('\n'.join(map(str, data)))
