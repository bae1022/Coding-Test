from collections import defaultdict

def solution(tickets):
    answer = []
    li = defaultdict(list) # 키가 존재하는지 따로 검사 안 해도 됨

    for ticket in tickets:
        li[ticket[0]].append(ticket[1])

    for key in li.keys():
        li[key].sort(reverse=True)

    land = ['ICN']
    while land:
        temp = land[-1]

        if not li[temp]: # temp 에서 출발하는 티켓이 없을 경우 (길이 끊어졌을 경우)
            answer.append(land.pop()) # pop() -> 마지막 값을 가져오고 삭제

        else:
            land.append(li[temp].pop())

    answer.reverse()
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])) # ["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])) # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
print(solution([["ICN", "BBB"],["ICN", "CCC"],["BBB", "CCC"],["CCC", "BBB"],["CCC", "ICN"]])) # ["ICN", "BBB", "CCC", "ICN", "CCC", "BBB"]