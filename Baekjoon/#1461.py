n, m = map(int, input().split()) # n: 책의 수, m: 세준인가 한 번에 들 수 있는 책의 수
books = list(map(int, input().split()))

book_minus = [] # 음수 거리에 있는 책들
book_plus = [] # 양수 거리에 있는 책들

for book in books:
    if book < 0:
        book_minus.append(book)

    else:
        book_plus.append(book)

book_plus.sort(reverse=True)
book_minus.sort()

abs_max = 0 # 절댓값이 큰 수
for i in books:
    if abs(i) > abs(abs_max):
        abs_max = i

result_list = []
for i in range(0, len(book_plus), m):
    if book_plus[i] != abs_max:
        result_list.append(book_plus[i])

for i in range(0, len(book_minus), m):
    if book_minus[i] != abs_max:
        result_list.append(abs(book_minus[i]))

result = abs(abs_max)
for l in result_list:
    result += (l * 2)

print(result)