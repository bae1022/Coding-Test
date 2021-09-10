n, score, p = map(int, input().split()) # n: 리스트에 있는 점수의 개수/score: 송유진의 새로운 점수/p: 랭킹 리스트에 올라갈 수 있는 점수의 개수

if n == 0:
    print(1)

elif p == 0:
    print(-1)

else:
    score_list = list(map(int, input().split()))  # 현지 랭킹 리스트에 있는 점수

    score_list.append(score)
    score_list.sort(reverse=True)

    if score_list.index(score) + 1 > p:
        print(-1)
    else:
        if score_list[-1] == score and n == p:
            print(-1)
        else:
            print(score_list.index(score) + 1)
