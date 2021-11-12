def solution(clothes):
    clothes.sort(key=lambda x:x[1])

    temp = clothes[0][1]

    clothe_type = {}
    clothe_type[temp] = 1
    for i in range(1, len(clothes)):
        if temp != clothes[i][1]:
            clothe_type[clothes[i][1]] = 1

            temp = clothes[i][1]

        else:
            clothe_type[clothes[i - 1][1]] += 1

    answer = 1
    for value in clothe_type.values():
        answer *= (value + 1)

    return answer - 1 # 아무것도 입지 않은 경우는 제외한다.

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
print(solution([["dd", "abc"]]))