from collections import defaultdict

def solution(record):
    answer = []
    temp = []

    users = defaultdict(set)

    for i in range(len(record)):
        r = record[i].split(" ")
        e = r[0]

        if e == 'Enter':
            user_id = r[1]
            name = r[2]

            users[user_id] = name

            temp.append(user_id + '님이 들어왔습니다.')
        elif e == 'Leave':
            user_id = r[1]

            temp.append(user_id + '님이 나갔습니다.')

        elif e == 'Change':
            user_id = r[1]
            name = r[2]

            users[user_id] = name

    for i in range(len(temp)):
        index = temp[i].find('님')

        answer.append(users[temp[i][:index]] + temp[i][index:])

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]