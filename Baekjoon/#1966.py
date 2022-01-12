case = int(input())

for i in range(case):
    n, m = map(int, input().split()) # 문서의 개수, 몇 번째로 인쇄되었는지 궁금한 문서

    docs = list(input().split())
    doc = []

    for j in range(len(docs)):
        doc.append((j, int(docs[j])))

    cnt = 0
    while doc:
        c, num = doc.pop(0)

        state = 0
        for k in range(len(doc)):
            if doc[k][0] == c and doc[k][1] == num:
                continue

            if doc[k][1] > num:
                doc.append((c, num))
                state = -1
                break

        if state == -1:
            continue

        elif c == m:
            break

    print(n - len(doc))