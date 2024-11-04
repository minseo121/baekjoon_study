read = input()
arr = []
for i in range(len(read)):
    arr.append(read[i:])
arr = sorted(arr)
print("\n".join(arr))