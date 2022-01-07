n = int(input())
answer = 0

for i in range(n):
    s = input()
    dict = {}

    start = ''
    state = 0
    for j in range(len(s)):
        if start != s[j]:
            if s[j] not in dict.keys(): # 사전에 없었던 경우
                dict[s[j]] = 1
                start = s[j]

            else: # 사전에 있었던 경우
                state = -1
                break

    if state == 0:
        answer += 1

print(answer)