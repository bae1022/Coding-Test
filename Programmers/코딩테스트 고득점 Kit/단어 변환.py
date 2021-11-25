from collections import deque

def solution(begin, target, words):
    answer = 0

    queue = deque()
    queue.append((begin, 0))

    visit = [-1] * len(words)
    counts = []

    while queue:
        temp, c = queue.popleft()

        if temp == target:
            counts.append(c)

        for n in range(len(words)):
            if visit[n] != -1 or temp == words[n]:
                continue

            cnt = 0

            for i in range(len(words[n])):
                if temp[i] == words[n][i]:
                    pass

                else:
                    cnt += 1

            if cnt >= 2:
                continue

            if cnt <= 1 and visit[n] == -1:
                queue.append((words[n], c + 1))
                visit[n] = 0

    if len(counts) == 0:
        answer = 0

    else:
        answer = min(counts)

    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])) # 0