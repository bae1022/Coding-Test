from collections import defaultdict
from itertools import combinations

t = int(input())

for _ in range(t):
    s = input()
    n = int(input())

    words = defaultdict(lambda: 0)
    index = defaultdict(list)

    for i in range(len(s)):
        words[s[i]] += 1

    for i in range(len(s)):
        if words[s[i]] >= n:
            index[s[i]].append(i) # 인덱스 기록

    if len(index) == 0:
        print(-1)

    else:
        long_answer = -1
        short_answer = 10001

        for key, value in index.items():
            if len(value) == 2 and n == 2:
                x, y = value[0], value[1]
                tmp = int(y) - int(x)

                if tmp > long_answer:
                    long_answer = tmp

                if tmp < short_answer:
                    short_answer = tmp

            else:
                tmp = -1
                for i in range(0, len(value) - (n - 1)):
                    tt = value[i + (n - 1)] - value[i]

                    if tt > long_answer:
                        long_answer = tt

                    if tt < short_answer:
                        short_answer = tt

        print(short_answer + 1, long_answer + 1)