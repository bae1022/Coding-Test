s = list(map(str, input().split()))

for i in range(len(s)):
    word = s[0]
    state = 0
    alpha = ''

    if i > 0:
        b = s[i][:-1]

        for j in range(-1, -len(s[i]), -1):

            if (ord(b[j]) >= 65 and ord(b[j]) <= 90) or (ord(b[j]) >= 97 and ord(b[j]) <= 122): # 대문자 A부터 소문자 z까지 (처음 발견)
                if state == 0:
                    word += ' '

                    alpha += b[j]
                    state = 1
                else:
                    alpha += b[j]

            else:
                if b[j] == '[':
                    word += ']'

                elif b[j] == ']':
                    word += '['

                else:
                    word += b[j]

        word += alpha[::-1]
        word += ';'

        print(word)