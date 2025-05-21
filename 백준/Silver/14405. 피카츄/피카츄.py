import sys

s = str(input())
data = ["pi", "ka", "chu"]
result = ""
i = 0

while i < len(s):
    if i < len(s) - 1 and s[i] == "p" and s[i + 1] == "i":
        result = "YES"
        i += 2
    elif i < len(s) - 1 and s[i] == "k" and s[i + 1] == "a":
        result = "YES"
        i += 2
    elif i < len(s) - 2 and s[i] == "c" and s[i + 1] == "h" and s[i + 2] == "u":
        result = "YES"
        i += 3
    else:
        result = "NO"
        break
        
sys.stdout.write(result)
