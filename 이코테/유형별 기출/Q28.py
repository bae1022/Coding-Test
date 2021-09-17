n = int(input())

n_list = list(map(int, input().split()))

def find(array, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == mid:
        return mid

    elif array[mid] >= mid:
        return find(array, start, mid - 1)

    else:
        return find(array, mid + 1, end)

result = find(n_list, 0, n - 1)

if result == None:
    print(-1)
else:
    print(result)