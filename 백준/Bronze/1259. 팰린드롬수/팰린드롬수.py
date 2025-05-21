import sys

result = []

while True:
    data = sys.stdin.readline().strip()
    if data == "0":
        break

    if data == data[::-1]:  # 문자열을 뒤집어서 비교
        result.append("yes")
    else:
        result.append("no")

sys.stdout.write("\n".join(result) + "\n")
