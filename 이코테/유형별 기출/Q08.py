s = str(input())

words = []
nums = []
for i in range(len(s)):
    if s[i].isalpha():
        words.append(s[i])

    else:
        nums.append(int(s[i]))

words.sort()
print(*words, sep='', end='')
print(sum(nums))