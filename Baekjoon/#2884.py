h, m = map(int, input().split())

if m < 45: # 분이 45분보다 작으면
    answer_m = 60 + m - 45

    if h == 0:
        answer_h = 23
    else:
        answer_h = h - 1

else:
    answer_m = m - 45
    answer_h = h

print(answer_h, answer_m)
