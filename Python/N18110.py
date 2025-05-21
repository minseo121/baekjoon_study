import sys

def my_round(val):
    if val - int(val) >= 0.5:
        return int(val)+1
    else:
        return int(val)

n = int(sys.stdin.readline().strip())

if n == 0:
    sys.stdout.write("0\n")
else:
    data = []
    for _ in range(n):
        data.append(int(sys.stdin.readline().strip()))
    
    data.sort()

    top = my_round(n * 0.15)

    trimmed_data = data[top:n-top]  # 위, 아래 각각 'top'만큼 제거
    result = my_round(sum(trimmed_data) / len(trimmed_data))

    sys.stdout.write(f"{result}\n")
