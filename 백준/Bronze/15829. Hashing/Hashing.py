l = int(input())
m = 1234567891
r = 31
input = input()

answer = 0

for i in range(len(input)):
    num = ord(input[i])-96
    answer += num * (r**i)

print(answer%m)