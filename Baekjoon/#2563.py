n = int(input())

paper = [[0] * 101 for _ in range(101)]

for k in range(n):
    a, b = map(int, input().split())

    for i in range(a, a + 10):
        for j in range(b, b + 10):
            paper[i][j] = 1

answer = 0

for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            answer += 1

print(answer)