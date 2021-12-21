from itertools import permutations

def solution(user_id, banned_id):
    answer = 0

    l = list(permutations(user_id, len(banned_id)))

    def check(user, ban):
        for i in range(len(ban)):
            if len(ban[i]) != len(user[i]):
                return False

            elif len(ban[i]) == len(user[i]):
                for j in range(len(user[i])):
                    if user[i][j] == ban[i][j] or ban[i][j] == '*':
                        continue

                    else:
                        return False

        return True

    result = []
    for users in l:
        if check(users, banned_id) is True:
            users = set(users)

            if users not in result:
                result.append(users)

        else:
            continue

    answer = len(result)

    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
# print(solution(["fradi"], ["frady"]))