from collections import defaultdict

def solution(n, words):
    answer = []

    dict = defaultdict(list)

    state = 0
    start = ''
    for i in range(len(words)):
        num = i

        if i >= n:
            num = i % n

        if i > 0 and start != words[i][0]:
            answer.append(num + 1)
            answer.append(len(dict[num]) + 1)
            state = 1
            break

        for key, value in dict.items():
            if words[i] in value:
                state = 1
                break

        dict[num].append(words[i])
        start = words[i][-1]

        if state == 1:
            answer.append(num + 1)
            answer.append(len(dict[num]))
            break

    if state == 0:
        answer.append(0)
        answer.append(0)

    return answer

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])) # [2, 3]
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])) # [0, 0]
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])) # [1, 3]