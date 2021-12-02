from collections import defaultdict

def solution(skill, skill_trees):
    answer = 0

    skill_list = defaultdict(list)

    for i in range(len(skill)):
        skill_list[skill[i]] = i

    for i in range(len(skill_trees)):
        state = 0
        tree = skill_trees[i]

        temp = 0
        for j in range(len(tree)):
            k = skill_list.get(tree[j])

            if k is not None:
                t = skill_list[tree[j]]

                if temp == t:
                    temp += 1

                else:
                    state = 1
                    break

        if state == 0:
            answer += 1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])) # 2