str1, str2 = map(str, input().split()) # 길이는 str1 <= str2

min_cnt = 51
# 한 칸씩 밀면서 같은지 본다.
for i in range(len(str2) - len(str1) + 1):
    cnt = 0

    for j in range(len(str1)):
        if str1[j] != str2[i + j]:
            cnt += 1

    if cnt < min_cnt:
        min_cnt = cnt

print(min_cnt)