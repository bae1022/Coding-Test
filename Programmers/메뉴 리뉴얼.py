from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []

    menu = defaultdict(list)

    for c in course:
        menu = {}

        for order in orders:
            if len(order) >= c:
                m = list(combinations(order, c))

                for i in range(len(m)):
                    s = list(m[i])
                    s.sort()
                    s = ''.join(s)

                    if s in menu:
                        menu[s] += 1

                    else:
                        menu[s] = 1

        if len(menu) != 0:
            tmp = max(menu.values())

            for key, value in menu.items():
                if value == tmp and tmp != 1:
                    answer.append(''.join(key))

    answer.sort()

    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))