def solution(cacheSize, cities):
    answer = 0

    s = dict()

    def get_key(val):
        for key, value in s.items():
            if val == value:
                return key

    if cacheSize == 0:
        answer = len(cities) * 5

    else:
        for city in cities:
            city = city.lower()

            if city not in s.keys(): # city가 캐시에 없을 경우
                if len(s) >= cacheSize: # 캐시가 이미 다 찼을 경우
                    dic_max = max(s.values()) # value가 가장 큰 값 도출

                    t = get_key(dic_max) # value값에 해당하는 key 찾음
                    s.pop(t) # 해당 key를 지움

                    s[city] = 0 # 키값 넣음

                    answer += 5 # 없던 값이므로 수행시간 5 추가

                else: # 캐시가 다 차지 않았을 경우
                    s[city] = 0
                    answer += 5

            else: # city가 캐시 값에 있을 경우
                answer += 1
                s[city] = 0

            for k, v in s.items():
                s[k] += 1

    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))