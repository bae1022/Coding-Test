from collections import defaultdict


def solution(id_list, report, k):
    answer = [0] * len(id_list)

    report = set(report)
    report = list(report)  # 중복 신고 제거

    count = defaultdict(list)

    for i in range(len(report)):
        r = report[i].split(' ')
        x, y = r[0], r[1]  # x: 신고하는 사람, y: 신고 당한 사람
        count[y].append(x)

    name_dict = defaultdict()
    for i in range(len(id_list)):
        name_dict[id_list[i]] = i

    for key, value in count.items():
        if len(value) >= k:

            for v in value:
                answer[name_dict[v]] += 1

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))