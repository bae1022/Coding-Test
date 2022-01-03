from collections import defaultdict

def solution(msg):
    answer = []

    nums = defaultdict(list)
    nums = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
        'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

    complete = []
    cnt = 26

    idx_start = 0
    idx_end = 1

    limit = len(msg)

    while idx_end <= limit:
        tmp = msg[idx_start:idx_end]

        if tmp in nums.keys():
            if idx_end == limit:
                d = nums[msg[idx_start:idx_end]]
                answer.append(d)
                break

            else:
                idx_end += 1
                continue

        else:
            cnt += 1
            nums[tmp] = cnt

            d = nums[msg[idx_start:(idx_end - 1)]]
            answer.append(d)

            idx_start = idx_end - 1

    return answer

print(solution("KAKAO")) # [11, 1, 27, 15]
print(solution("TOBEORNOTTOBEORTOBEORNOT")) # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
print(solution("ABABABABABABABAB")) # [1, 2, 27, 29, 28, 31, 30]