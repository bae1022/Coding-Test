n, k = map(int, input().split())  # n: 멀티탭 구멍의 개수/ k: 전기 용품의 총 사용횟수
names = list(map(int, input().split()))

plug = []  # 현재 멀티탭에 꼽혀 있는 플러그

answer = 0
for i in range(k):
    if names[i] in plug:
        continue

    elif names[i] not in plug and len(plug) < n:
        plug.append(names[i])
        continue

    multi_indexs = []
    state = False
    for j in range(n):
        if plug[j] in names[i:]:  # 멀티탭 안에 플러그 값이 있음
            multi_index = names[i:].index(plug[j])

        else:  # 멀티탭 안에 플러그 값이 존재하지 않음
            multi_index = 101
            state = True

        multi_indexs.append(multi_index)

        if state is True:
            break

    plug_out = multi_indexs.index(max(multi_indexs)) # 멀티탭 안에 존재하지 않는 플러그 값이나 가장 나중에 꽂힐 플러그
    del plug[plug_out]  # 플러그에서 제거

    plug.append(names[i])
    answer += 1

print(answer)
