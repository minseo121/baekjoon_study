import sys

data = []
result = []

while True:
    data = sys.stdin.readline().split()
    if data == ['0', '0', '0']:
        break
    a = int(data[0])
    b = int(data[1])
    c = int(data[2])
    if a*a + b*b == c*c or b*b + c*c == a*a or c*c+a*a==b*b:
        result.append('right')
        data = []
    else:
        result.append('wrong')
        data = []

sys.stdout.write("\n".join(map(str, result)) + "\n")