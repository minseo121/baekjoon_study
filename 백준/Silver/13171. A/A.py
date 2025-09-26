import sys
input = sys.stdin.readline

MOD = 1_000_000_007
A = int(input().strip()) % MOD
X = int(input().strip())

res = 1        
base = A       
exp = X        

while exp > 0:
    if exp % 2 == 1:              
        res = (res * base) % MOD  
    base = (base * base) % MOD    
    exp //= 2                     

print(res)
