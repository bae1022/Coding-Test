n = int(input()) # 반 학생 수

students = []
for i in range(n):
    name, score1, score2, score3 = map(str, input().split())
    students.append((name, int(score1), int(score2), int(score3)))

students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(students[i][0])