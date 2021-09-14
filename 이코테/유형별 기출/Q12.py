def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 기둥
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer: # 바닥위 or 보의 한 쪽 끝부분 위 or 다른 기둥 위
                continue

            return False

        elif stuff == 1: # 보
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue

            return False

    return True

def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, stuff, operate = frame

        if operate == 1: # 설치
            answer.append([x, y, stuff]) # 설치 해본 뒤

            if possible(answer) is not True:
                answer.remove([x, y, stuff]) # 가능한 구조물이 아니면 다시 제거

        elif operate == 0: # 제거
            answer.remove([x, y, stuff])

            if possible(answer) is not True:
                answer.append([x, y, stuff])

    return sorted(answer)

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))