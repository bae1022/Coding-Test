from collections import defaultdict


def solution(fees, records):
    answer = defaultdict(lambda: 0)
    cars = defaultdict(list)

    limit, pay, minute, plus_pay = fees[0], fees[1], fees[2], fees[3]

    for i in range(len(records)):
        time, num, state = records[i].split(' ')
        cars[num].append(time)

    for key, value in cars.items():
        if len(value) % 2 == 1:
            cars[key].append('23:59')

    for key, value in cars.items():
        start = ''
        end = ''
        time = 0

        for v in range(len(value)):
            if v % 2 == 0:  # 입차시간
                start = value[v]

            else:
                end = value[v]

            if start != '' and end != '':
                start = start.split(':')
                start_hour = int(start[0])
                start_minute = int(start[1])

                end = end.split(':')
                end_hour = int(end[0])
                end_minute = int(end[1])

                time += (end_hour * 60 + end_minute) - (start_hour * 60 + start_minute)  # 머문 시간(분 단위)

                start = ''
                end = ''

        if time <= limit:  # 기본요금 시간보다 작을 경우
            answer[key] += pay

        else:
            answer[key] += pay

            over = time - limit  # 초과된 시간

            if over % minute == 0:
                over = over // minute

            else:
                over = over // minute + 1

            answer[key] += (plus_pay * over)

    tmp = []

    for key, value in answer.items():
        tmp.append((key, value))

    tmp.sort(key=lambda x: x[0])

    result = []
    for i in range(len(tmp)):
        result.append(tmp[i][1])

    return result

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))