import sys
input = sys.stdin.read
data = input().strip()

result = []
i = 0

while i < len(data):
    if data[i] == '<':  
        while data[i] != '>':  
            result.append(data[i])
            i += 1
        result.append(data[i])  
        i += 1
    elif data[i].isalnum(): 
        start = i
        while i < len(data) and data[i].isalnum():  
            i += 1
        word = data[start:i]
        result.append(word[::-1])  
    else:  
        result.append(data[i])
        i += 1

print(''.join(result))