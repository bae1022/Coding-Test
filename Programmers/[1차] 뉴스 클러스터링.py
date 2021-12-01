from collections import Counter

def solution(str1, str2):
    answer = 0
    temp = 0

    str1_arr = []
    str2_arr = []

    for i in range(0, len(str1) - 1):
        t = str1[i:i + 2]

        if t.isalpha():
            str1_arr.append(t.lower())

        else:
            continue

    for i in range(0, len(str2) - 1):
        t = str2[i:i + 2]

        if t.isalpha():
            str2_arr.append(t.lower())

        else:
            continue

    if len(str1_arr) == 0 and len(str2_arr) == 0:
        temp = 1

    else:
        counter1 = Counter(str1_arr)
        counter2 = Counter(str2_arr)

        inter = list((counter1 & counter2).elements())
        union = list((counter1 | counter2).elements())

        temp = len(inter) / len(union)

    answer = int(65536 * temp)

    return answer

print(solution('FRANCE', 'french')) #16384
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))