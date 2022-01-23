while True:
    try:
        s1, s2 = map(str, input().split())
        answer = 0

        cnt = 0
        for i in range(len(s2)):
            if cnt == len(s1):
                answer = 1
                break

            if s2[i] == s1[cnt]:
                cnt += 1

        if cnt == len(s1) or answer == 1:
            print('Yes')

        else:
            print('No')

    except:
        break