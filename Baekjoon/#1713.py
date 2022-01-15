from collections import defaultdict

dic = defaultdict(lambda: 0) # dict 자료형 원하는 초기값 설정

n = int(input())
input()
data = map(int, input().split())

for k in data:
    if len(dic) == n and k not in dic.keys():
        key = list(dic.keys())
        val = list(dic.values())

        temp = val.index(min(val))
        idx = key[temp]

        del (dic[idx]) # 호출 횟수가 가장 적은 것 제거

    dic[k] += 1

print(*sorted(dic.keys()))

