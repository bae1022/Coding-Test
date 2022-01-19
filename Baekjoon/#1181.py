n = int(input())

words = []
for i in range(n):
    t = input()

    words.append((len(t), t))

words.sort(key=lambda x:(x[0], x[1]))

answer = []
for word in words:
    answer.append(word[1])

tmp = ''
for i in range(len(answer)):
    if tmp != answer[i]:
        print(answer[i])
        tmp = answer[i]