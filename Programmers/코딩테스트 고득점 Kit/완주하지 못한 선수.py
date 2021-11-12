def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    state = 0
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            state = 1
            break

    if state == 0:
        answer = participant[len(participant) - 1]

    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
