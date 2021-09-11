def solution(s):

    answer = 0

    n = len(s) // 2


    min_len = len(s)

    for i in range(1, n + 1):
        compressed = ""
        prev = s[:i]
        cnt = 1

        for j in range(i, len(s), i):
            if prev == s[j:j + i]:
                cnt += 1
            else:
                if cnt >= 2:
                    compressed += str(cnt) + prev
                else:
                    compressed += prev

                prev = s[j:j + i]
                cnt = 1

        if cnt >= 2:
            compressed += str(cnt) + prev
        else:
            compressed += prev

        if len(compressed) < min_len:
            min_len = len(compressed)

    answer = min_len
    return answer

print(solution('aabbaccc'))