def solution(genres, plays):
    answer = []

    albums = {} # 각각을 넣어놓는다
    album = {} # 합을 넣어놓는다

    for i in range(len(genres)):
        if genres[i] in album: # 장르가 앨범에 속해 있으면
            album[genres[i]] += plays[i]
            albums[genres[i]].append((i, plays[i]))

        else:
            album[genres[i]] = plays[i]
            albums[genres[i]] = [(i, plays[i])]

    album = sorted(album.items(), key=lambda x:-x[1])

    # print(album)
    # print(albums)
    for i in range(len(album)):
        t_list = albums[album[i][0]]
        t_list.sort(key=lambda x: (-x[1], x[0]))

        answer.append(t_list[0][0])

        if len(t_list) >= 2:
            answer.append(t_list[1][0])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print(solution(["classic", "pop", "classic", "classic", "classic"], [500, 1000, 400, 300, 200]))