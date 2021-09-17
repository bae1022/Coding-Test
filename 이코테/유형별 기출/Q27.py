n, x = map(int, input().split()) # n: n개의 원소를 포함 /x: x가 몇개인지?

n_list = list(map(int, input().split()))

def first(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if (mid == 0 or target > array[mid - 1]) and array[mid] == target: # 가장 왼쪽에 있는 값 반환
        return mid

    elif array[mid] >= target: # 중간점의 값보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
        return first(array, target, start, mid - 1)

    else: # 중간점의 값 보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        return first(array, target, mid + 1, end)

def last(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid

    elif array[mid] > target:
        return last(array, target, start, mid - 1)

    else:
        return last(array, target, mid + 1, end)

n1 = first(n_list, x, 0, n - 1)
n2 = last(n_list, x, 0, n - 1)

if n1 == None or n2 == None:
    print(-1)

else:
    print(n2 - n1 + 1)

