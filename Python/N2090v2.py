import sys
input = sys.stdin.readline

def getGcd(a,b):
    while b:
        a, b = b, a%b
    return a

def getLcm(a, b):
    return (a*b) // getGcd(a,b)

n = int(input().strip())
a = list(map(int, input().split()))
numer = 1
denom = a[0]

for i in range(1,n):
    ni, di = 1, a[i]
    lcm = getLcm(denom, a[i]) #두 수의 최소공배수를 구해서
    ni = (lcm // denom) * numer + (lcm//di) *ni #분모를 최소공배수로 만들때 되는 분자 구하기
    di = lcm #분모모
    gcd = getGcd(ni, di)
    numer = ni // gcd
    denom = di // gcd #기약분수로 만들기

print(str(denom) + '/'+ str(numer))
