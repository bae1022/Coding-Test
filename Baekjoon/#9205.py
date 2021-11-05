
INF = 1e9
t = int(input())

for i in range(t):
    store = int(input()) # 편의점의 개수
    points = []

    home_x, home_y = map(int, input().split())
    points.append((home_x, home_y))

    for j in range(store):
        store_x, store_y = map(int, input().split())
        points.append((store_x, store_y))

    festival_x, festival_y = map(int, input().split())
    points.append((festival_x, festival_y))

    dp = [[INF] * (store + 2) for _ in range(store + 2)] # 편의점, 집, 페스티벌을 모두 저장

    for a in range(store + 2):
        for b in range(store + 2):
            if a == b:
                # dp[a][b] = 5
                continue

            if abs(points[a][0] - points[b][0]) + abs(points[a][1] - points[b][1]) <= 1000:
                dp[a][b] = 1

    for c in range(store + 2):
        for a in range(store + 2):
            for b in range(store + 2):
                if dp[a][b] > dp[a][c] + dp[c][b]:
                    dp[a][b] = dp[a][c] + dp[c][b]

    if dp[0][store + 2 - 1] > 0 and dp[0][store + 2 - 1] < INF:
        print('happy')
    else:
        print('sad')

