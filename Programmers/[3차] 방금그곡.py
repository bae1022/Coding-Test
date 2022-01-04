def solution(m, musicinfos):
    answer = ''
    result = []

    while '#' in m:
        m = m.replace('C#', 'c')
        m = m.replace('D#', 'd')
        m = m.replace('E#', 'e')
        m = m.replace('F#', 'f')
        m = m.replace('G#', 'g')
        m = m.replace('A#', 'a')
        m = m.replace('B#', 'b')

    for info in musicinfos:
        start, finish, title, melody = info.split(',')

        start_info = start.split(':')
        finish_info = finish.split(':')

        running = ((int(finish_info[0]) * 60) + int(finish_info[1])) - ((int(start_info[0]) * 60) + int(start_info[1]))

        while '#' in melody:
            melody = melody.replace('C#', 'c')
            melody = melody.replace('D#', 'd')
            melody = melody.replace('E#', 'e')
            melody = melody.replace('F#', 'f')
            melody = melody.replace('G#', 'g')
            melody = melody.replace('A#', 'a')
            melody = melody.replace('B#', 'b')

        result_melody = ''

        i = 0
        cnt = 0

        while cnt < running:
            if i >= len(melody):
                index = i % len(melody)

            else:
                index = i

            result_melody += melody[index]
            cnt += 1

            i += 1

        if m in result_melody:
            result.append((title, running))

        else:
            continue

    if len(result) == 0:
        answer = "(None)"

    else:
        result.sort(key=lambda x:-x[1])
        answer = result[0][0]

    return answer

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])) #"HELLO"
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CCB", ["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"]))