n, m = map(int, input().split()) # n = 박스의 개수/m = 책의 개수

box = list(map(int, input().split()))
book = list(map(int, input().split()))

print(sum(box) - sum(book))