n, k = map(int, input().split()) # n: 국가의 수, k: 등수를 알고 싶은 국가

countries = []

for _ in range(n):
    num, gold, silver, bronze = map(int, input().split())

    countries.append((num, gold, silver, bronze))

    if num == k:
        find_country = ((num, gold, silver, bronze))


sort_countries = sorted(countries, key = lambda x: (-x[1], -x[2], -x[3]))

rank = 1
i = 0

while True:
    find_country_gold = find_country[1]
    find_country_silver = find_country[2]
    find_country_bronze = find_country[3]

    if find_country_gold == sort_countries[i][1] and find_country_silver == sort_countries[i][2] and find_country_bronze == sort_countries[i][3]:
        break

    i += 1
    rank += 1

print(rank)

