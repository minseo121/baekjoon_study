import sys
input = sys.stdin.readline

N, B, H, W = map(int, input().split())
results = []

for _ in range(H):
    p = int(input().strip())
    a = list(map(int, input().split()))

    for i in a:
        if i >= N:
            price = p*N
            if price <= B:
                results.append(price)
        
if not results:
    print("stay home")
else:
    print(min(results))
    