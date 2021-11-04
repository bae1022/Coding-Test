s = input()

answer = [0] * 26

for i in range(len(s)):
    n = ord(s[i]) - 97

    answer[n] += 1

print(*answer, sep=' ')