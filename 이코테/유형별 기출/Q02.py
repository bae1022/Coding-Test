s = str(input())

result = int(s[0])

for i in range(1, len(s)):
    n = int(s[i])

    if n <= 1 or result <= 1:
        result += n

    else:
        result *= n

print(result)