array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0 , 5, 2]

count = [0] * (max(array) + 1) # 0부터 9까지의 데이터가 있다.

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스 증가

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')

